import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    drop_menu = st.selectbox("What topic do you want to discuss", (df["topic"]))
    text_area_message = st.text_area("Your Message")
    message =f"""\
Subject: ({drop_menu}) New email from {user_email}

{text_area_message}

From: {user_email}
"""
    button = st.form_submit_button("Send")
    if button:
        print(message)
        send_email(message)
        st.info("Your email was sent successfully!")