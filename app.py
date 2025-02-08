import streamlit as st
# from presidio_analyzer import AnalyzerEngine
# from presidio_anonymizer import AnonymizerEngine


# Title of the app
st.title("Simple Streamlit App")

# Text input for the user's name
user_name = st.text_input("Enter your name:")

# Button to greet the user
if st.button("Say Hello"):
    if user_name:
        st.write(f"Hello, {user_name}! 👋")
    else:
        st.write("Please enter your name!")
