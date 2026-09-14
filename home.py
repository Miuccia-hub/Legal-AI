import streamlit as st

st.title("LAWS90286")

name=st.text_input("What is your name?")
age_input=st.text_input("What is your age?")
person={
    "name":name,
    "age":age_input,
}
if st.button("Say hi"):
    st.write(f"Hello, {name}, welcome to my world.")
if age_input:
    age = int(age_input)
    if age<=26:
        st.write("You were born this millenium.")
    else:
        st.write("You were born last millenium.")