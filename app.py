import streamlit as st
from transformers import pipeline 

model = pipeline("text-generation", model="openai-gpt")

def main():
    st.set_page_config(page_title="My Hugging Face App", page_icon=":rocket:", layout='wide')
    
    with st.sidebar:
        st.title("Settings")
        text_input = st.text_area("Message LLM...")

    st.title("🚀 Streamlit App with a Hugging Face Model")
    
    if st.button("Enter"):
        if text_input:
            with st.spinner("Generating..."):
                generated_text = model(text_input, max_length=50, do_sample=True)[0]['generated_text']
            st.markdown("### Response")
            st.write(generated_text)
        else:
            st.warning("Input Required")

if __name__ == "__main__":
    main()
