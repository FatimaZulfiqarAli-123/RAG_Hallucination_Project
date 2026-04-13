from retriever import create_vectorstore, retrieve

db = create_vectorstore()

def rag_qa(question):
    docs = retrieve(question, db)

    if not docs:
        return "I don't know based on documents.", ""

    #  ONLY return relevant sentence
    answer = docs[0].page_content.strip()

    return answer, answer