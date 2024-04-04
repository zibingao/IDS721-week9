import streamlit as st
from transformers import pipeline

st.title('Hugging Face LLM Streamlit App')

generator = pipeline('text-generation', model='gpt-2')
user_input = st.text_input("Type a sentence...")

if st.button('Generate Text'):
    generated_text = generator(user_input, max_length=100)[0]['generated_text']
    st.text_area("Generated Text", value=generated_text, height=250)
