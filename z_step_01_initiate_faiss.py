import sub_langchain_loader_pdf as my_pdf
import sub_text_spliter as my_spliter
import sub_FAISS as my_faiss

listTextPages = my_pdf.read_pdf()
listTextSegments = my_spliter.get_text_segments(listTextPages)
my_faiss.create_and_save_faiss(listTextSegments)

print("complete")