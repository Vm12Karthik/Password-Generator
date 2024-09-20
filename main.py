
import streamlit as st
import random


# Define function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

def generate_password(length):
    # Define the character set
    character_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+=-"
    
    password = ''.join(random.sample(character_set, length))
    
    return password

def main():

    st.title("Random Password Generator")
    st.write("This app generates a random password based on the length you specify.")

    password_length = st.slider("Select password length you want:", min_value=6, max_value=30, value=10, step=1)

    if st.button("Generate Password"):

        password = generate_password(password_length)
    
        st.success(f"### Your random password is: \n ### {password}")

if __name__ == "__main__":
    main()