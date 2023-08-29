import streamlit as st
import db

d=db.fetch_user()
with st.expander("See the data"):
    st.write(d)

def SignUp():
    with st.form(key="SignUp"):
        user=st.text_input("Enter Yout Username")
        Fullname=st.text_input("Enter Yout Full name")
        email=st.text_input("Enter Yout Email ID")
        password=st.text_input("Enter Yout Password",type="password")
        re_password=st.text_input("Re-Enter Yout Password",type="password")

        if st.form_submit_button("Submit"):
            if password==re_password:
                        
                db.insert_user(user,Fullname,email,password)
                st.info("User successfully inserted")
                st.balloons()

with st.container():
    login,signup=st.tabs(["Login", "SignUp"])

    with login:
        st.write("Login ")
    with signup:
        SignUp()
