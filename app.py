app_code = """
# app.py
import streamlit as st, tempfile
from agent import load_vector_store, build_qa_chain, query_has_med, make_rxnorm_answer, ask_llm

st.set_page_config(page_title="PharmaPal", page_icon="💊", layout="centered")

st.title("💊 PharmaPal — Medication Q&A (Free & Open Source)")
st.caption("General, non-diagnostic medication answers using RxNorm + Gemini (optional). Not medical advice.")

query = st.text_input("Ask a medication question")

uploaded = st.file_uploader("Upload PDFs (optional, for doc-based Q&A)", type="pdf", accept_multiple_files=True)

vectordb = None; qa_chain = None
if uploaded:
    with st.spinner("Indexing document..."):
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        tmp.write(uploaded[0].read())
        tmp.flush()        # make sure everything is written
        tmp.close()        # close so PyPDF can open it

        import os
        print("File size:", os.path.getsize(tmp.name))  # ✅ debug check

        vectordb = load_vector_store(tmp.name)
        qa_chain = build_qa_chain(vectordb)

if st.button("Get Answer") and query:
    is_med, rxcui, data = query_has_med(query)
    if is_med and rxcui:
        with st.spinner("Fetching RxNorm data..."):
            st.success(make_rxnorm_answer(query, rxcui, data))
    elif qa_chain:
        with st.spinner("Searching your document..."):
            st.info(qa_chain.run(query))
    else:
        with st.spinner("Using LLM fallback..."):
            st.write(ask_llm(query))

st.markdown("---")
st.markdown("⚠ Disclaimer: PharmaPal provides general information only. For medical decisions, consult a healthcare professional.")
"""
with open("app.py", "w") as f:
    f.write(app_code)
