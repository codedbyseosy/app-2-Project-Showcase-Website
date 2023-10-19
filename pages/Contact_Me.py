import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area() #this allows us to enter multiple lines of text as opposed to a single line
    button = st.form_submit_button() #special button design to submit its assigned form
    print(button)
    if button:
        print("Pressed")