%%writefile agent.py
# agent.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool, AgentType
import os
from dotenv import load_dotenv

# Load your environment variables
load_dotenv()

# Set up Gemini model
llm = ChatGoogleGenerativeAI(
    model='models/gemini-1.5-pro-002',
    temperature=0.5,
    google_api_key=os.environ['GOOGLE_API_KEY']
)

# Simulated tool functions
def check_prescription_status(query):
    return "✅ Your prescription for Amoxicillin is approved and ready for refill."

def set_reminder(query):
    return "⏰ Medication reminder set for 8:00 AM daily."

def get_pharmacy_hours(query):
    return "🕘 The pharmacy is open from 9 AM to 7 PM, Monday through Saturday."

def current_refills_available(query):
    return "💊 You have 2 refills available for your blood pressure medication."

def refill_request(query):
    return "📦 Your refill request for Atorvastatin has been successfully submitted."

def check_drug_interaction(query):
    return "🩺 There are no known interactions between Ibuprofen and your current medications."

# Tool list
tools = [
    Tool(name="CheckPrescriptionStatus", func=check_prescription_status,
         description="Use this tool when the user asks about the status of a prescription."),
    Tool(name="SetReminder", func=set_reminder,
         description="Use this tool to set medication reminders for the user."),
    Tool(name="PharmacyHours", func=get_pharmacy_hours,
         description="Use this tool to provide pharmacy opening and closing hours."),
    Tool(name="RefillsAvailable", func=current_refills_available,
         description="Use this tool to check how many refills the user has left."),
    Tool(name="RefillRequest", func=refill_request,
         description="Use this tool when the user requests a new medication refill."),
    Tool(name="DrugInteraction", func=check_drug_interaction,
         description="Use this tool when the user asks about drug interactions or safety."),
]

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(query):
    try:
        return agent.run(query)
    except Exception as e:
        return f"❌ Error: {e}"
