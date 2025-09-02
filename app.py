import streamlit as st
from agent import run_agent

st.set_page_config(page_title='PharmaPal Chatbot', layout='centered')
st.title('💊 PharmaPal: Prescription Refill & Reminder Chatbot')
st.write('Ask about refills, reminders, pharmacy hours, and more.')

user_query = st.text_input('What would you like to ask PharmaPal?', '')

if st.button('Ask'):
    if user_query.strip():
        with st.spinner('Thinking...'):
            response = run_agent(user_query)
            st.success(response)
