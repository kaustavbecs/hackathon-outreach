import time
import requests
import boto3
import streamlit as st
from langchain.chains import ConversationChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory

st.title("Email Generator")

# Setup bedrock
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

# Load the prompt from file
def load_prompt_from_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

@st.cache_resource
def load_llm():
    llm = Bedrock(client=bedrock_runtime, model_id="anthropic.claude-v2")
    llm.model_kwargs = {"temperature": 0.1, "max_tokens_to_sample": 2048}

    model = ConversationChain(llm=llm, verbose=True, memory=ConversationBufferMemory())

    return model

model = load_llm()

if st.button('Call Support API'):
    response = requests.get('https://7cxxu7h62f.execute-api.us-east-1.amazonaws.com/Dev/support')
    st.write(response.json())

if st.button('Call Cost API'):
    response = requests.get('https://7cxxu7h62f.execute-api.us-east-1.amazonaws.com/Dev/cost')
    st.write(response.json())

prompt_path1 = 'email_prompt1.txt'  # Path to the file containing the prompt
email_prompt1 = load_prompt_from_file(prompt_path1)

prompt_path2 = 'email_prompt2.txt'  # Path to the file containing the prompt
email_prompt2 = load_prompt_from_file(prompt_path2)

# Create variables to store the generated email content
generated_email_one = ""
generated_email_two = ""

# Create a column layout for the buttons and text areas
col1, col2 = st.columns(2)

with col1:
    if st.button('Generate Email for Customer One'):
        if email_prompt1:
            # Generate response and simulate typing
            response = model.predict(input=email_prompt1)
            generated_email_one = response
            st.text_area("Email Content for Customer One:", value=generated_email_one, height=900)
        else:
            st.error("Please ensure the email prompt file contains content.")

with col2:
    if st.button('Generate Email for Customer Two'):
        if email_prompt2:
            # Generate response and simulate typing
            response = model.predict(input=email_prompt2)
            generated_email_two = response
            st.text_area("Email Content for Customer Two:", value=generated_email_two, height=900)
        else:
            st.error("Please ensure the email prompt file contains content.")
