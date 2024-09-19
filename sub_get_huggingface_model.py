# https://python.langchain.com/v0.2/docs/integrations/platforms/huggingface/
# pip install langchain-huggingface


import os, getpass

from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

#from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

def get_chat_model():
    if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = getpass.getpass("Enter your HuggingFace token: ")

    llm = HuggingFaceEndpoint(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    )

    chat_model = ChatHuggingFace(llm=llm)
    return chat_model