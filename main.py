# https://streamlit.io/#install
# pip install streamlit

import streamlit as st
import z_step_03_chatbot as my_chat

def main():
    chat_chain = my_chat.get_conversational_chain()
    vector_store = my_chat.my_faiss.load_faiss()

    #response = my_chat.user_input("What is the purpose", vector_store=vector_store, chat_chain=chat_chain)

    st.set_page_config(page_title="Chat PDF", page_icon=":file_pdf:")  # Set title and icon

    #st.header("<h1 style='color: #3498db; text-align: center;'>Chat with PDF using Gemini</h1>", unsafe_allow_html=True)  # Colored header with center alignment
    st.header("Chat with PDF by HD")  # Colored header with center alignment

    #user_question = st.text_input("**Ask a Question from the PDF Files**", key="question_input", style="font-size: 18px; padding: 10px; border: 1px solid #ddd; border-radius: 5px;")  # Styled text input

    user_question = st.text_input("**Ask a Question from the PDF Files**", key="question_input")  # Styled text input


    if user_question:
        response = my_chat.user_input(user_question, vector_store=vector_store, chat_chain=chat_chain)
        st.write("Reply: ", response["output_text"])

    with st.sidebar:
        st.title("This is a test by HD")
        #st.title("<h3 style='color: #2ecc71;'>Menu:</h3>", unsafe_allow_html=True)  # Green colored sidebar title

        # pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)

        #if st.button("Submit & Process"):  # Styled button
        #    with st.spinner("Processing..."):
        #        response = my_chat.user_input(user_question, vector_store=vector_store, chat_chain=chat_chain)
        #        st.write("Reply: ", response["output_text"])
        #    st.success("Done!")

if __name__ == "__main__":
    main()