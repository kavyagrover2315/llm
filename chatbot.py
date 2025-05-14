import requests
import os
import streamlit as st

# Get API key from environment
api = os.environ.get('gsk_zZnX3OCMkH3whD1PJ5kFWGdyb3FYfg1Aq0zfmztrwOoJRTQU3KSls')
if not api:
    st.error("GROQ_API_KEY environment variable not set.")
    st.stop()

# Chatbot logic
def chatbot(user_query):
    url = 'https://api.groq.com/openai/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api}',
        'Content-Type': 'application/json'
    }

    parameters = {
        'model': 'gemma2-9b-it',
        'messages': [
            {
                'role': 'system',
                'content': 'You are an AI assistant that explains user inputs in great detail using clear and extended responses.'
            },
            {
                'role': 'user',
                'content': user_query
            }
        ],
        'temperature': 0.9,
        'max_tokens': 1500
    }

    try:
        response = requests.post(url, headers=headers, json=parameters)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Chat with Groq AI (Streamlit)")

user_input = st.text_input("Enter your query:", placeholder="Ask me anything...")
if st.button("Get Answer") and user_input:
    with st.spinner("Thinking..."):
        response = chatbot(user_input)
    st.text_area("Response:", response, height=300)
