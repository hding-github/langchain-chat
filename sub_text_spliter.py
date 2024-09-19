from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
    ],
    # Existing args
)

text_splitter_t = CharacterTextSplitter(
    # shows how to seperate
    separator="\n",
    # Shows the document token length
    chunk_size=1000,
    # How much overlap should exist between documents
    chunk_overlap=150,
    # How to measure length
    length_function=len
)

# To remove \n newline from the content
def remove_chars(doc, strChars = '\n'):
    #text = page.page_content.replace(strChars,'')
    text = doc.replace(strChars, "")
    return text

def get_text_segments(text_pages):
    listTextSegments = list()
    for page in text_pages:
        # Applying the splitter
        #docs = text_splitter.split_documents(page)
        #texts = text_splitter.create_documents([page.content])
        strText = page.page_content
        #docs = text_splitter.split_text(strText)

        docs = strText.split('\n \n')
        
        # applied on the docs
        for strSentences in docs:
            if len(strSentences)>1:
                strT = remove_chars(strSentences)
                listTextSegments.append(strT)
    return listTextSegments