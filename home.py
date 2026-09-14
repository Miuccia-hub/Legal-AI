import streamlit as st

st.title("LAWS90286")

name=st.text_input("What is your name?")
person={
    "name":name,
}
if st.button("Say hi"):
    st.write(f"Hello, {name}, welcome to my world.")

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# 自动从 .env 文件读取变量到环境变量中
load_dotenv()
client = OpenAI()
response = client.responses.create(
    model="gpt-4o",
    input=f"Write a poem about {name}.",
)
st.write(response.output_text)