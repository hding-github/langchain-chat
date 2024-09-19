# https://python.langchain.com/v0.2/docs/integrations/platforms/huggingface/
# pip install langchain-huggingface


import os, getpass

from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

#from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate


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


from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(
        content="What happens when an unstoppable force meets an immovable object?"
    ),
]

ai_msg = chat_model.invoke(messages)
print(ai_msg.content)

if False:
    messages = [
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(
            content="My name is Hunter."
        ),
    ]

    ai_msg = chat_model.invoke(messages)
    print(ai_msg.content)


    messages = [
        SystemMessage(content="You're a helpful assistant"),
        HumanMessage(
            content="What is my name."
        ),
    ]

    ai_msg = chat_model.invoke(messages)
    print(ai_msg.content)



print("completed")


