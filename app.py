import streamlit as st
from transformers import pipeline

# Load the language model
model = pipeline("text-generation", model="openai-gpt")


# Define Streamlit app
def main():
    st.title("Language Model Deployment with Streamlit")
    text_input = st.text_area("Enter text to generate continuation:")

    if st.button("Generate"):
        if text_input:
            generated_text = model(text_input, max_length=50, do_sample=True)[0][
                "generated_text"
            ]
            st.write("Generated Text:")
            st.write(generated_text)
        else:
            st.warning("Please enter some text first.")


if __name__ == "__main__":
    main()
