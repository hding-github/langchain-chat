# https://python.langchain.com/v0.2/docs/integrations/vectorstores/faiss/

# pip install --upgrade --quiet  langchain sentence_transformers
#from langchain_huggingface import HuggingFaceEmbeddings
#import sentence_transformers

from langchain_huggingface.embeddings import HuggingFaceEmbeddings

#embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-mpnet-base-v2")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

#embeddings = HuggingFaceEmbeddings(model=sentence_transformers)

#pip install faiss-cpu
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from uuid import uuid4
from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
    ],
    # Existing args
)

index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))

def convert_text_segments_to_docs(listTextSegments, strSource = "test_doc"):
    listDocs = list()
    tDoc = Document(
        page_content="Building an exciting new project with LangChain - come check it out!",
        metadata={"source": "tweet"},
    )
    listDocs.append(tDoc)
    return listDocs

def create_vector_store():
    vector_store = FAISS(
        embedding_function=embeddings,
        index=index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )
    return vector_store

def create_and_save_faiss(listText, strSource = "pdf", strFileName = "faiss_index"):
    vector_store = create_vector_store()
    docs = list()
    for strText in listText:
        tDoc = Document(page_content=strText, metadata={"source": strSource},)
        docs.append(tDoc)

    uuids = [str(uuid4()) for _ in range(len(docs))]

    vector_store.add_documents(documents=docs, ids=uuids)

    faiss_vector_db = FAISS.from_documents(docs, embeddings)
    faiss_vector_db.save_local(strFileName)

def load_faiss(strFileName = "faiss_index"):
    vector_store = FAISS.load_local(
        strFileName, embeddings, allow_dangerous_deserialization=True
    )
    return vector_store

