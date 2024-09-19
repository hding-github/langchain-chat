import sub_FAISS as my_faiss

vector_store = my_faiss.load_faiss()

results = vector_store.similarity_search_with_score(
    "Is driving of a motor vehicle a complex task.", k=1, filter={"source": "pdf"})
for res, score in results:
    print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")

print("Complete.")