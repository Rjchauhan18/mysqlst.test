
import os
import streamlit as st
from deta import Deta
import datetime
from dotenv import load_dotenv
load_dotenv(".env")
key =os.getenv('Deta_key')
st.write(key)
deta= Deta(key)


db=deta.Base("auth")

def insert_user(username,email,password):
    date_join=str(datetime.datetime.now()) 
    db.put({"Username":username,"EmailID":email,"Password":password,"Date of join":date_join})


def fetch_user():
    users=db.fetch()
    return users.items

d=fetch_user()
st.write(d)

user=st.text_input("Enter Yout username")
email=st.text_input("Enter Yout Email ID")
password=st.text_input("Enter Yout Password",type="password")

if st.button("submit"):
    insert_user(user,email,password)
    st.info("User successfully inserted")
    st.balloons()
    
