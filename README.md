# 🤖 Reducing Hallucinations in Retrieval-Augmented Question Answering Systems

> **A Retrieval-Augmented Generation (RAG) based Question Answering system designed to improve factual reliability by grounding AI-generated answers in retrieved documents.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![FAISS](https://img.shields.io/badge/FAISS-Semantic%20Search-orange)](https://faiss.ai/)
[![NLP](https://img.shields.io/badge/NLP-Question%20Answering-green)](https://en.wikipedia.org/wiki/Natural_language_processing)
[![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented%20Generation-purple)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)

---

## 📌 Overview

Large Language Models (LLMs) can sometimes generate information that appears plausible but is not supported by factual evidence. This phenomenon, commonly known as **AI hallucination**, is a major challenge for reliable Question Answering systems.

This project explores how **Retrieval-Augmented Generation (RAG)** can help reduce hallucinations by providing the question-answering system with relevant external context before generating an answer.

The project implements and compares two approaches:

1. **Basic Question Answering** — generates answers without retrieving external documents.
2. **Retrieval-Augmented Question Answering** — retrieves relevant information using a **FAISS-based semantic search pipeline** and uses the retrieved context to support answer generation.

The system additionally incorporates **confidence scoring and hallucination analysis** to assess the reliability of generated responses.

---

## 🎯 Objectives

The main objectives of this project are to:

* Build a document-based Question Answering system.
* Implement semantic document retrieval using FAISS.
* Develop a Retrieval-Augmented Generation pipeline.
* Compare Basic QA with Retrieval-Augmented QA.
* Reduce unsupported or hallucinated responses.
* Ground generated answers in relevant document context.
* Introduce confidence scoring for generated answers.
* Analyze the likelihood of hallucination.
* Improve the factual reliability of AI-generated responses.

---

## 🧠 Core Concept

The key idea behind this project is simple:

```text
Basic QA
Question → Model → Answer
```

The model must rely primarily on information already available to it.

In contrast:

```text
RAG QA
Question
   ↓
Retrieve Relevant Documents
   ↓
Relevant Context
   ↓
Question + Context
   ↓
Model
   ↓
Grounded Answer
```

By retrieving relevant information before generating an answer, the system can provide the model with additional context that supports the response.

---

# ⚙️ System Architecture

The overall architecture of the project consists of document processing, embedding, retrieval, answer generation, and reliability analysis.

```text
                         Documents
                            │
                            ▼
                  ┌───────────────────┐
                  │ Text Processing   │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Text Embeddings   │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │   FAISS Index     │
                  │ Semantic Search   │
                  └─────────┬─────────┘
                            │
                            │
User Question ──────────────┤
                            ▼
                  ┌───────────────────┐
                  │ Relevant Context  │
                  │    Retrieval      │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Question Answering│
                  │      System       │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Answer +          │
                  │ Confidence Score  │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Hallucination     │
                  │ Analysis          │
                  └───────────────────┘
```

---

# 🔍 System Workflow

### 1. Document Loading

The system begins by loading documents from the provided dataset.

These documents serve as the external knowledge source for the retrieval-based QA system.

---

### 2. Text Embedding

The document text is converted into numerical vector representations using an embedding-based NLP approach.

These vectors capture semantic information about the documents and allow the system to compare the meaning of a user query with document content.

---

### 3. FAISS Indexing

The generated embeddings are stored in a **FAISS index**.

FAISS enables efficient similarity search over vector representations.

When a user submits a question, the system searches the index for documents or passages that are semantically similar to the query.

---

### 4. Context Retrieval

The most relevant information is retrieved from the indexed documents.

```text
User Query
    ↓
Query Embedding
    ↓
FAISS Similarity Search
    ↓
Relevant Documents / Context
```

The retrieved context is then passed to the RAG-based Question Answering pipeline.

---

### 5. Answer Generation

The project compares two approaches.

#### Basic QA

```text
Question → QA Model → Answer
```

The answer is generated without retrieving information from the project documents.

#### RAG QA

```text
Question
   ↓
FAISS Retrieval
   ↓
Relevant Context
   ↓
Question + Context
   ↓
QA Model
   ↓
Answer
```

The RAG approach provides additional context to support the generated answer.

---

### 6. Confidence Scoring

The system includes a confidence scoring component to provide an indication of how reliable a generated answer may be.

The confidence analysis can be used alongside retrieval information to evaluate the quality of the response.

---

### 7. Hallucination Analysis

A dedicated hallucination analysis component is used to investigate whether generated answers are sufficiently supported by the available information.

The project therefore goes beyond simply generating an answer and attempts to assess **answer reliability and factual grounding**.

---

# ⚖️ Basic QA vs. RAG QA

| Aspect                      | Basic QA | RAG QA   |
| --------------------------- | -------- | -------- |
| External document retrieval | ❌ No     | ✅ Yes    |
| Semantic search             | ❌ No     | ✅ Yes    |
| FAISS                       | ❌ No     | ✅ Yes    |
| Retrieved context           | ❌ No     | ✅ Yes    |
| Grounded answers            | Limited  | Improved |
| Hallucination analysis      | ✅        | ✅        |
| Confidence scoring          | ✅        | ✅        |

The central purpose of the comparison is to investigate whether providing retrieved contextual information can improve the factual reliability of Question Answering.

---

# 📊 Key Features

* 📚 **Document-based Question Answering**
* 🔎 **Semantic Document Retrieval**
* ⚡ **FAISS Similarity Search**
* 🤖 **Retrieval-Augmented Generation**
* ⚖️ **Basic QA vs. RAG QA Comparison**
* 📉 **Hallucination Analysis**
* 📊 **Confidence Scoring**
* 🧠 **NLP-based Text Representation**
* 🔗 **Context-Grounded Answer Generation**

---

# 🛠️ Technologies Used

| Technology           | Purpose                                     |
| -------------------- | ------------------------------------------- |
| **Python**           | Core programming language                   |
| **FAISS**            | Efficient vector similarity search          |
| **NLP**              | Text processing and semantic representation |
| **Embeddings**       | Numerical representation of text            |
| **Machine Learning** | Question-answering and retrieval pipeline   |
| **Git/GitHub**       | Version control and project management      |

---

# 📂 Project Structure

```text
Reducing-Hallucinations-RAG/
│
├── main.py
│   └── Main project pipeline
│
├── retriever.py
│   └── Document retrieval and FAISS search
│
├── qa_basic.py
│   └── Basic Question Answering implementation
│
├── qa_rag.py
│   └── Retrieval-Augmented Question Answering implementation
│
├── confidence.py
│   └── Confidence scoring component
│
├── hallucination.py
│   └── Hallucination analysis component
│
├── requirement.txt
│   └── Project dependencies
│
├── RAG_Hallucination.pdf
│   └── Detailed project report
│
├── output 01.JPG
│   └── Example system output
│
├── .gitignore
│   └── Git ignored files
│
└── README.md
    └── Project documentation
```

---

# 🖥️ Example Output

The project includes an example output demonstrating the system's Question Answering process.

![RAG Question Answering Output](output%2001.JPG)

---

# 📄 Project Report

A detailed explanation of the project methodology, implementation, and analysis is available in the accompanying project report.

📥 **[View / Download the RAG Hallucination Project Report](RAG_Hallucination.pdf)**

The report provides additional information about the implemented system and its experimental analysis.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/FatimaZulfiqarAli-123/reducing-hallucinations-rag.git
```

Then navigate to the project directory:

```bash
cd reducing-hallucinations-rag
```

> Replace the repository URL above with your actual GitHub repository URL if the repository name is different.

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirement.txt
```

---

# ▶️ Run the Project

Execute the main pipeline using:

```bash
python main.py
```

The system will process the documents, perform retrieval, generate answers, and perform the corresponding confidence and hallucination analysis according to the implemented pipeline.

---

# 🔬 Research Motivation

Hallucination is one of the major challenges associated with reliable AI systems.

A model may produce a fluent and convincing response even when the information is unsupported by the available evidence.

This project investigates a practical approach to this problem:

> **Can retrieving relevant information before answering make Question Answering systems more reliable?**

By comparing a Basic QA system with a retrieval-augmented approach, the project demonstrates the role that external knowledge retrieval can play in improving answer grounding.

---

# 💡 Potential Applications

Retrieval-Augmented Question Answering can be applied to:

* 📚 Educational Question Answering
* 🏢 Enterprise Knowledge Bases
* 📄 Document Question Answering
* 🔬 Research Assistance
* 💬 Customer Support Systems
* ⚖️ Knowledge-intensive applications
* 🏥 Domain-specific information systems
* 🗂️ Internal organizational documentation

---

# 🔮 Future Improvements

Several improvements could make the system more robust and suitable for larger-scale applications:

* Use stronger sentence/document embedding models.
* Experiment with different retrieval strategies.
* Implement hybrid keyword + semantic retrieval.
* Add document chunking and metadata filtering.
* Experiment with modern Transformer-based LLMs.
* Introduce reranking of retrieved documents.
* Evaluate retrieval precision and recall.
* Add automated factuality evaluation.
* Compare multiple hallucination detection techniques.
* Introduce citation-based answer generation.
* Evaluate the system on larger and more diverse datasets.
* Develop a Streamlit or API-based interface.
* Optimize FAISS indexing for large document collections.

---

# ⚠️ Limitations

Although RAG can improve factual grounding, retrieval alone does not completely eliminate hallucinations.

Potential limitations include:

* Incorrect retrieval can lead to incorrect answers.
* Poor-quality documents can affect answer quality.
* Embedding quality influences retrieval performance.
* The model may still generate information not supported by the retrieved context.
* Confidence scores should not automatically be interpreted as factual certainty.
* Hallucination detection remains a challenging NLP problem.

Therefore, retrieval should be considered an important component of a reliable QA pipeline rather than a complete solution to hallucination.

---

# 📈 Evaluation

A comprehensive evaluation of the system can consider both **retrieval quality** and **answer quality**.

### Retrieval Evaluation

Possible metrics include:

* Recall@K
* Precision@K
* Mean Reciprocal Rank (MRR)

### Answer Evaluation

Possible metrics include:

* Exact Match
* F1-score
* Semantic similarity
* Answer faithfulness
* Context relevance

### Hallucination Evaluation

The system can additionally compare:

```text
Basic QA
     vs.
RAG QA
```

to investigate whether retrieved context reduces unsupported responses.

> Specific performance values should be added here once experimentally measured.

---

# 🤝 Contribution

Contributions and suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a pull request.

---

# 📜 License

This project is intended primarily for **educational and research purposes**.

Please ensure that any datasets, pretrained models, and third-party libraries used with the project comply with their respective licenses.

---

# 👩‍💻 Author

**Fatima Zulfiqar Ali**

Machine Learning & NLP Enthusiast

Interested in:

* 🤖 Artificial Intelligence
* 🧠 Natural Language Processing
* 🔎 Retrieval-Augmented Generation
* 📚 Question Answering
* 🗣️ Multilingual NLP
* 🔬 NLP Research

---

# ⭐ Acknowledgements

This project explores the use of **retrieval-augmented techniques** to improve the reliability and factual grounding of AI-powered Question Answering systems.

If you find this project useful, consider giving the repository a ⭐.
