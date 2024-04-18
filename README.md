
### Prerequisite commands to run:

```bash
conda create --name myenv 
conda info --envs
conda activate myenv
pip install streamlit
```

### Configure local AWS CLI - you should be able to run "aws s3 ls"


### Chatbot

To interact with a chatbot built using Amazon Bedrock, LangChain, and Streamlit, run:

```bash
streamlit run chat_bedrock_st.py
```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.