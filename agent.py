agent_code = """
# agent.py
import os, re, requests
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

llm = None
embeddings = None
if GOOGLE_API_KEY:
    llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-pro", temperature=0.2, google_api_key=GOOGLE_API_KEY)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

# Fallback dummy embeddings if Gemini not available
if embeddings is None:
    class DummyEmb:
        def embed_documents(self, docs): return [[0.0]] * len(docs)
    embeddings = DummyEmb()

# ---------- RAG ----------
def load_vector_store(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    chunks = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
    return FAISS.from_documents(chunks, embedding=embeddings)

def build_qa_chain(vectordb):
    retr = vectordb.as_retriever(search_kwargs={"k": 3})
    return RetrievalQA.from_chain_type(llm=llm, retriever=retr)

# ---------- RxNorm ----------
RXNAV_BASE = "https://rxnav.nlm.nih.gov/REST"

def rxnorm_search(name):
    try:
        r = requests.get(f"{RXNAV_BASE}/drugs.json", params={"name": name}, timeout=8)
        r.raise_for_status()
        return r.json()
    except: return None

def get_rxcui(data):
    try:
        for g in data.get("drugGroup", {}).get("conceptGroup", []):
            if g.get("conceptProperties"):
                return g["conceptProperties"][0]["rxcui"], g["conceptProperties"][0]["name"]
    except: return (None, None)
    return (None, None)

def rxnorm_props(rxcui):
    try:
        r = requests.get(f"{RXNAV_BASE}/rxcui/{rxcui}/properties.json", timeout=8)
        r.raise_for_status()
        return r.json()
    except: return None

def query_has_med(query):
    data = rxnorm_search(query)
    if not data: return (False, None, None)
    rxcui, name = get_rxcui(data)
    return (bool(rxcui), rxcui, data)

def make_rxnorm_answer(query, rxcui, data):
    props = rxnorm_props(rxcui)
    out = []
    if props and "properties" in props:
        p = props["properties"]
        out.append(f"Name: {p.get('name')}")
        if p.get("synonym"): out.append(f"Synonym: {p['synonym']}")
        if p.get("strength"): out.append(f"Strength: {p['strength']}")
    else:
        out.append("Results:")
        for g in data.get("drugGroup", {}).get("conceptGroup", []):
            for cp in g.get("conceptProperties", [])[:3]:
                out.append(f"- {cp.get('name')} (rxcui {cp.get('rxcui')})")
    out.append("\\nNote: General info only. Not medical advice.")
    return "\\n".join(out)

def ask_llm(prompt):
    if llm:
        try: return llm.predict(prompt)
        except: return "LLM error"
    return "LLM not configured"
"""
with open("agent.py", "w") as f:
    f.write(agent_code)
