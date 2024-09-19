# https://python.langchain.com/v0.2/docs/integrations/vectorstores/faiss/

# pip install --upgrade --quiet  langchain sentence_transformers
#from langchain_huggingface import HuggingFaceEmbeddings
#import sentence_transformers

from langchain_huggingface.embeddings import HuggingFaceEmbeddings

#embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-mpnet-base-v2")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

#embeddings = HuggingFaceEmbeddings(model=sentence_transformers)

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

if False:
    from uuid import uuid4

    from langchain_core.documents import Document

    document_1 = Document(
        page_content="I had chocalate chip pancakes and scrambled eggs for breakfast this morning.",
        metadata={"source": "tweet"},
    )

    document_2 = Document(
        page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
        metadata={"source": "news"},
    )

    document_3 = Document(
        page_content="Building an exciting new project with LangChain - come check it out!",
        metadata={"source": "tweet"},
    )

    document_4 = Document(
        page_content="Robbers broke into the city bank and stole $1 million in cash.",
        metadata={"source": "news"},
    )

    document_5 = Document(
        page_content="Wow! That was an amazing movie. I can't wait to see it again.",
        metadata={"source": "tweet"},
    )

    document_6 = Document(
        page_content="Is the new iPhone worth the price? Read this review to find out.",
        metadata={"source": "website"},
    )

    document_7 = Document(
        page_content="The top 10 soccer players in the world right now.",
        metadata={"source": "website"},
    )

    document_8 = Document(
        page_content="LangGraph is the best framework for building stateful, agentic applications!",
        metadata={"source": "tweet"},
    )

    document_9 = Document(
        page_content="The stock market is down 500 points today due to fears of a recession.",
        
    )

    document_10 = Document(
        page_content="I have a bad feeling I am going to get deleted :(",
        metadata={"source": "tweet"},
    )

    documents = [
        document_1,
        document_2,
        document_3,
        document_4,
        document_5,
        document_6,
        document_7,
        document_8,
        document_9,
        document_10,
    ]
    uuids = [str(uuid4()) for _ in range(len(documents))]

    vector_store.add_documents(documents=documents, ids=uuids)

    results = vector_store.similarity_search_with_score(
        "Will it be hot tomorrow?", k=1, filter={"source": "news"}
    )
    for res, score in results:
        print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")


    results = vector_store.similarity_search(
        "LangChain provides abstractions to make working with LLMs easy",
        k=2,
        filter={"source": "tweet"},
    )
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")


    vector_store.save_local("faiss_index")

    new_vector_store = FAISS.load_local(
        "faiss_index", embeddings, allow_dangerous_deserialization=True
    )

    results = new_vector_store.similarity_search("What can LangChain do?")
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")