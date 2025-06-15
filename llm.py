import requests
import streamlit as st

# ✅ Groq API key (use securely in production)
api_key = "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"

# ✅ Chatbot function
def chatbot(user_query):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",  # ✅ A known working model on Groq
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that explains things clearly and in detail."},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ✅ Streamlit UI
st.set_page_config(page_title="Groq AI Chatbot", layout="centered")
st.title("🤖 Chat with Groq AI (LLaMA-3)")

user_input = st.text_input("💬 Ask a question:", placeholder="Ask me anything...")

if st.button("🚀 Get Answer") and user_input.strip():
    with st.spinner("Thinking..."):
        result = chatbot(user_input)
    st.text_area("📢 AI's Response:", value=result, height=300)
