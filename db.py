import os
from deta import Deta
from dotenv import load_dotenv
import datetime

load_dotenv(".env")
DETA_KEY =os.getenv("DETA_KEY")
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
