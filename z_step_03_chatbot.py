#import streamlit as st
#from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
#from langchain_google_genai import GoogleGenerativeAIEmbeddings
#import google.generativeai as genai

#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS

#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

import sub_get_huggingface_model as my_chat_model
import sub_FAISS as my_faiss

def get_conversational_chain():
    prompt_template = """
    Answer the question in as detailed manner as possible from the provided context, make sure to provide all the details, if the answer is not in the provided
    context then just say, "answer is not available in the context", dont provide the wrong answer\n\n
    Context:\n {context}?\n
    Question:\n {question}\n

    Answer:
    """
    #model = ChatGoogleGenerativeAI(model = "gemini-pro",temperature = 0.3)
    model = my_chat_model.get_chat_model()

    prompt = PromptTemplate(template= prompt_template,input_variables=["context","question"])
    chain = load_qa_chain(model, chain_type = "stuff",prompt = prompt)
    return chain

def user_input(user_question, vector_store, chat_chain):
    #embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    #new_db = FAISS.load_local("faiss_index", embeddings)
    docs = vector_store.similarity_search(user_question)

    #chain = get_conversational_chain()

    
    response = chat_chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print("***************************")
    print(response["output_text"])
    #st.write("Reply: ", response["output_text"])
    return (response)

chat_chain = get_conversational_chain()
vector_store = my_faiss.load_faiss()

response = user_input("What is the purpose", vector_store=vector_store, chat_chain=chat_chain)
print(response["output_text"])
print("complete")