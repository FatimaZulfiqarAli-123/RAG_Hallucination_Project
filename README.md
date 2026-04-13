# 🧠 Reducing Hallucinations in Retrieval-Augmented Question Answering Systems

## 📌 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based Question Answering system to reduce hallucinations in AI-generated responses.

It compares two approaches:
- Basic Question Answering (without retrieval)
- Retrieval-Augmented Question Answering (with FAISS-based retrieval)

The system improves response accuracy by grounding answers in relevant retrieved documents instead of relying only on model memory.

---

## 🎯 Objectives

- Build a document-based QA system using retrieval techniques
- Reduce hallucinations in generated answers
- Compare performance of:
  - Basic QA system
  - RAG-based QA system
- Introduce confidence scoring for answers
- Improve reliability and factual accuracy of responses

---

## ⚙️ Technologies Used

- Python 🐍
- FAISS (for efficient similarity search)
- NLP techniques for embedding & retrieval
- Basic ML/NLP-based QA pipeline

---

## 🔍 System Workflow

1. Load documents from dataset
2. Convert text into embeddings
3. Store embeddings using FAISS index
4. Retrieve relevant context for user query
5. Generate answer using:
   - Basic QA (no retrieval)
   - RAG QA (with retrieved context)
6. Compute confidence score
7. Detect hallucination probability

---

## 📊 Key Features

- 📚 Document-based question answering
- 🔎 Semantic search using embeddings
- 🤖 Retrieval-Augmented Generation pipeline
- 📉 Hallucination detection module
- 📊 Confidence scoring system
- ⚖️ Comparison between Basic QA and RAG QA

---

## 📄 Project Report

A detailed explanation of the project is included in the report.

📥 **Download Report:**  
👉 [RAG Hallucination Project Report (PDF)](./RAG_Hallucination.pdf)

---

## 🚀 How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirement.txt
