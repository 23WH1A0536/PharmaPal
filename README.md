# 💊 PharmaPal – AI-Powered Prescription Refill & Medication Assistant

PharmaPal is an **Agentic AI-powered healthcare chatbot** developed as a student project to simplify medication management. It helps users request prescription refills, set medication reminders, check prescription status, and access pharmacy-related information through an intelligent conversational interface.

The latest version integrates **Retrieval-Augmented Generation (RAG)** for more accurate, context-aware responses and supports **multilingual conversations**, making the chatbot more accessible and user-friendly.

---

## ✨ Features

- 💬 AI-powered conversational chatbot
- 💊 Request prescription refills
- ⏰ Set medication reminders
- 📄 Check prescription status
- 🏥 Access pharmacy information
- 🌍 Multilingual support
- 📚 RAG-based knowledge retrieval for accurate responses
- 🤖 Agentic workflow using LangChain
- 🎨 Interactive Streamlit interface

---

## 🚀 How It Works

1. The user interacts with PharmaPal through a **Streamlit web interface**.
2. **Google Gemini** understands the user's request.
3. A **LangChain Agent** determines the appropriate action.
4. **RAG** retrieves relevant information from the knowledge base.
5. Simulated pharmacy and scheduling APIs handle refill requests, reminders, and prescription status.
6. Gemini generates a context-aware response in the user's preferred language.

---

## 🏗️ Architecture

```
User
   │
   ▼
Streamlit Interface
   │
   ▼
Google Gemini
   │
   ▼
LangChain Agent
   │
   ├── RAG Knowledge Base
   ├── Pharmacy API
   ├── Reminder Scheduler
   └── Prescription Status API
   │
   ▼
Response
```

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini
- LangChain
- Retrieval-Augmented Generation (RAG)
- Vector Database
- Simulated Pharmacy APIs

---

## 📂 Project Structure

```
PharmaPal/
│── app.py
│── requirements.txt
│── chatbot/
│── rag/
│── data/
│── vector_store/
│── utils/
│── assets/
│── README.md
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
cd PharmaPal
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Add your Google API key:

```text
GOOGLE_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## 🌐 Multilingual Support

PharmaPal supports multiple languages, allowing users to interact in their preferred language while receiving accurate and context-aware responses.

---

## 📚 RAG Integration

The chatbot uses **Retrieval-Augmented Generation (RAG)** to improve response quality by retrieving relevant information from a knowledge base before generating answers. This helps provide more reliable and context-aware responses.

---

## 🤖 Agentic AI Workflow

Instead of following fixed chatbot responses, PharmaPal uses an Agentic AI approach where it:

- Understands user intent
- Selects the appropriate tools
- Retrieves relevant information using RAG
- Interacts with pharmacy-related services
- Generates intelligent, context-aware responses

---

## 💡 Sample Queries

- Refill my prescription.
- Remind me to take my medicine every day at 8 PM.
- What is the status of my prescription?
- Find the nearest pharmacy.
- Explain this medicine in Telugu.

---

## 🚀 Future Enhancements

- Voice-based interaction
- Real pharmacy API integration
- Appointment booking
- Medicine interaction checking
- Email and SMS reminders
- Personalized health recommendations
- Enhanced multilingual support
