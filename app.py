# streamlit_app.py

import streamlit as st
from deta import Deta
import datetime
Deta_key ="d0tfyvz8ygw_Q3L9xn7PkZmmCQQzhFK9atpNn5TA5iG5"

deta= Deta(Deta_key)


db=deta.Base("auth")

def insert_user(username,email,password):
    date_join=str(datetime.datetime.now()) 
    db.put({"Username":username,"EmailID":email,"Password":password,"Date of join":date_join})


user=st.text_input("Enter Yout username")
email=st.text_input("Enter Yout Email ID")
password=st.text_input("Enter Yout Password",type="password")

if st.button("submit"):
    insert_user(user,email,password)
    st.info("User successfully inserted")
    st.balloons()
# # Initialize connection.
# conn = st.experimental_connection('mysql', type='sql')

# # Perform query.
# df = conn.query('SELECT * from users;', ttl=600)

# for row in df.itertuples():
#     st.write(row)
#     # st.write(f"{row.name} has a :{row.pet}:")