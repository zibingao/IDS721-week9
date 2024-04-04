import streamlit as st
from transformers import pipeline

model = pipeline("text-generation", model="openai-gpt")

def main():
    st.title("🚀 Streamlit App with a Hugging Face Model")
    text_input = st.text_area("Message LLM...")

    if st.button("Enter"):
        if text_input:
            generated_text = model(text_input, max_length=50, do_sample=True)[0][
                "generated_text"
            ]
            st.write("Response")
            st.write(generated_text)
        else:
            st.warning("Input Required")

if __name__ == "__main__":
    main()
