
#https://python.langchain.com/v0.2/docs/integrations/document_loaders/pypdfloader/
#pip install -qU langchain_community pypdf

from langchain_community.document_loaders import PyPDFLoader

if False:
    from langchain_community.document_loaders.csv_loader import CSVLoader

    loader = CSVLoader(
        ...  # <-- Integration specific parameters here
    )

def read_pdf():
    loader = PyPDFLoader("./folder_pdf_files/Purpose.pdf",)
    data = loader.load()

    pages = []
    for doc in loader.lazy_load():
        pages.append(doc)

        print(doc.page_content)
        print(doc.metadata)
    
    intLen = len(pages)
    print("The number of text segements (n) = ", str(intLen))
    return pages

print("complete")