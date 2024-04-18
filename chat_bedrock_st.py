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
    llm.model_kwargs = {"temperature": 0.7, "max_tokens_to_sample": 2048}

    model = ConversationChain(llm=llm, verbose=True, memory=ConversationBufferMemory())

    return model

model = load_llm()

if st.button('Call Support API'):
    response = requests.get('https://7cxxu7h62f.execute-api.us-east-1.amazonaws.com/Dev/support')
    st.write(response.json())

if st.button('Call Cost API'):
    response = requests.get('https://7cxxu7h62f.execute-api.us-east-1.amazonaws.com/Dev/cost')
    st.write(response.json())

prompt_path = 'email_prompt.txt'  # Path to the file containing the prompt
email_prompt = load_prompt_from_file(prompt_path)

if st.button('Generate Email'):
    if email_prompt:
        message_placeholder = st.empty()  # Create an empty placeholder for dynamic updates
        full_response = ""

        # Generate response and simulate typing
        response = model.predict(input=email_prompt)
        words = response.split()  # Split response into words
        for word in words:
            full_response += word + ' '
            if word.endswith(('.', '!', '?')):
                full_response += "\n\n"  # Add newlines after sentences for better readability
            time.sleep(0.05)  # Sleep to mimic typing speed
            message_placeholder.text_area("Email Content:", value=full_response, height=300)

    else:
        st.error("Please ensure the email prompt file contains content.")
