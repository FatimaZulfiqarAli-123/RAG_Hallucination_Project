from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# ===============================
# Load documents properly
# ===============================
def load_documents():
    with open("data/documents.txt", "r", encoding="utf-8") as f:
        return f.readlines()   # ✅ each line is separate

# ===============================
# Build vector store
# ===============================
def create_vectorstore():
    docs = load_documents()

    # ✅ IMPORTANT FIX: treat each line as separate chunk
    splitter = CharacterTextSplitter(
        chunk_size=1,
        chunk_overlap=0
    )

    texts = []
    for d in docs:
        cleaned = d.strip()
        if cleaned:
            texts.append(cleaned)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_texts(texts, embeddings)
    return db

# ===============================
# Retrieve ONLY best match
# ===============================
def retrieve(query, db):
    results = db.similarity_search(query, k=1)
    return results