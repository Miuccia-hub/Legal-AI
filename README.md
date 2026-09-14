 # saving code
1. source control
2. client to add files to the commit
3. enter a commit message
4. click commit
5. click sync changes
6. click repository to confirm

 # setup environment
1. create a virtual environment
>python -m venv .venv
2. activate
>source /workspaces/Legal-AI/.venv/bin/activate
3. install streamlit 
>pip install streamlit
4. create a python file
>touch home.py
5. run st
>streamlit run home.py
6. edit the python file
>import streamlit as st

# 防止privacy上传到github
1. 创建.env
2. .gitignore
3. 在.gitignore里加入.env
4. 粘贴API Key

# use OpenAI
1. access the secret via key from .env
>pip install python-dotenv
>from dotenv import load_dotenv
>add load_dotenv in your code file
2. from dotenv import load_dotenv
3. from openai import OpenAI
4. set up openAI client
> client = OpenAI()
> response = client-responses.create(
    model="gpt-40",
    input=f"Write a poen about (name).",
)
> st.write(response.output_text)