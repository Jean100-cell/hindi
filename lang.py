
# multilingual_companion.py

import streamlit as st
from google.generativeai import GenerativeModel, configure

# --- Your Gemini API key directly (or use dotenv if needed)
GEMINI_API_KEY = "AIzaSyCqzY2VImY7KaTWSLqfQth86DacZFkDSMI"
configure(api_key=GEMINI_API_KEY)

# --- Streamlit Page Setup
st.set_page_config(page_title="🗣️ Multilingual Conversational Companion")
st.title("🌍 Multilingual Conversational Companion")
st.markdown("Practice conversations, get corrections and learn vocabulary — powered by Gemini AI.")

# --- Language selection
language = st.selectbox("Choose your target language:", ["Hindi", "Tamil", "French", "Spanish", "German"])

# --- Input from user
user_input = st.text_area(f"What would you like to say in {language}?", placeholder="Type your sentence or question here...", height=150)

# --- Simulate Conversation
if st.button("💬 Start Conversation"):
    if user_input.strip():
        prompt = f"""
        Act like a language tutor. The user is learning {language}. 

        1. First, respond to what they said.
        2. Then correct them (if needed) and give suggestions.
        3. Add 2-3 useful vocabulary tips based on the conversation.
        4. Keep the tone friendly and educational.

        User said: "{user_input}"
        """
        model = GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        st.subheader("🤖 Gemini's Response")
        st.markdown(response.text)
    else:
        st.warning("Please enter some text to begin the conversation.")
