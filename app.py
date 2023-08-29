import streamlit as st
import db
import re
import streamlit_authenticator as stauth

    
d=db.fetch_user()

status=None

def app(un):
    st.write(f'hello {un}  ')
    if st.sidebar.button('Logout'):
        st.session_state.status=False
        st.experimental_rerun()
    

 
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

 
    if(re.fullmatch(regex, email)):
        return "Valid Email"
 
    else:
        return "Invalid Email"
# def login():
        
#     return username,authetication_status,email

def SignUp():
    with st.form(key="SignUp"):
        user=st.text_input("Enter Yout Username")
        Fullname=st.text_input("Enter Yout Full name")
        email=st.text_input("Enter Yout Email ID")
        password=st.text_input("Enter Yout Password",type="password")
        re_password=st.text_input("Re-Enter Yout Password",type="password")

       
        if st.form_submit_button("Submit"):
            if password==re_password:
                e=check(email)
                if e=="Valid Email":
                    if db.get_user(user) != None:
                        st.warning("Username already in Exist !!!")
                    else:
                        if len(user) >3:
                            if len(password) >6:
                                # Hashed_password = stauth.Hasher([password]).generate()
                                db.insert_user(user,Fullname,email,password)
                                st.success("Account successfully Created !!!")
                                st.balloons()
                            else:
                                st.warning("Password should be at least 6 characters")
                        else:
                            st.warning("Username is too short")   
                else:
                    st.warning("Invalid Email ID")
            else:
                st.error("Password does not match")

                        
if 'status' not in st.session_state:
    st.session_state.status=status


if st.session_state.status==False or st.session_state.status==None:
    with st.container():
        login,signup=st.tabs(["Login", "SignUp"])

        with login:
            with st.form(key="Login"):
                username= st.text_input( 'Username')
                password= st.text_input('Password',type='password')
    
                if st.form_submit_button('Login'):
                    try:
                        loggedIn_user=db.get_user(username)

                    except:
                        pass

                    if loggedIn_user !=None:
                        
                        if loggedIn_user["Password"] == password:
                            st.session_state.status=True
                            st.session_state.un=loggedIn_user["key"]

                            st.info("You have successfully logged In")
                            # st.stop()
                            st.experimental_rerun()
                        else:
                            st.error("Incorrect Password")
                        
                    else:
                        st.error("Invalid Username")

                    
        with signup:
            SignUp()


elif st.session_state.get('status')==True:
            app(st.session_state.get('un'))
