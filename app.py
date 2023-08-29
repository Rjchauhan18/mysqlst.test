import streamlit as st
# import db
import os
from deta import Deta
from dotenv import load_dotenv
import datetime

load_dotenv(".env")
DETA_KEY =os.getenv("DETA_KEY")
st.write(DETA_KEY)
print(DETA_KEY)
# st.write(DETA_KEY)
deta= Deta(DETA_KEY)


db=deta.Base("auth")

def insert_user(username,full_name,email,password):
    date_join=str(datetime.datetime.now()) 
    db.put({"key":email,"Usename":username,"Fullname":full_name,"Password":password,"Date of join":date_join})


def fetch_user():
    users=db.fetch()
    return users.items

d=fetch_user()
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
                        
                insert_user(user,Fullname,email,password)
                st.info("User successfully inserted")
                st.balloons()

with st.container():
    login,signup=st.tabs(["Login", "SignUp"])

    with login:
        st.write("Login ")
    with signup:
        SignUp()
