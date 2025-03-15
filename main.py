import streamlit as st # importing the streamlit library for creating the web app
import random  # importing the random library for geanerating random characters
import string  # importing the string library for using string characters

#function to generate a password based on the user's preferences
def generate_password(length,use_digits,use_special):
    
    char=string.ascii_letters # include all letters (a-z and A-Z)    
    
    if use_digits:
        char+=string.digits # include numbers (0-9)
        
    if use_special:
        char+=string.punctuation # include special characters
        
    # generates a random password of the specified length using the characters defined above     
    return "".join(random.choice(char)for _ in range(length)) 

st.title("Password Generator")
length=st.slider("Select Pasword Length",min_value=6,max_value=32,value=12)

use_digits=st.checkbox("Include Digits")

use_special=st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password=generate_password(length,use_digits,use_special)
    st.success(f"Generated Password: `{password}`")

st.write("-------------------------------")
