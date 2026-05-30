# 🎥 YouTube RAG Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to chat with YouTube videos using AI.

The system extracts video transcripts, converts them into embeddings, stores them in ChromaDB, retrieves relevant content using semantic search, and generates context-aware responses using Llama3.

---

## 🚀 Features

* Extracts transcripts directly from YouTube videos
* Supports Hindi and English transcripts
* Splits transcripts into manageable chunks
* Generates embeddings using Sentence Transformers
* Stores embeddings in ChromaDB
* Performs semantic search for relevant context retrieval
* Uses Llama3 via Ollama for answer generation
* Provides context-aware responses from video content
* Suggests follow-up questions related to the topic

---

## 🛠️ Tech Stack

* Python
* Ollama
* Llama3
* ChromaDB
* Sentence Transformers
* YouTube Transcript API

---

## 🧠 RAG Pipeline

```text
YouTube URL
      ↓
Transcript Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
ChromaDB
      ↓
Semantic Retrieval
      ↓
Context Building
      ↓
Llama3
      ↓
AI Response
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd YoutubeRAG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and Llama3 is available:

```bash
ollama pull llama3
```

Run the application:

```bash
python app.py
```

---

## 💬 Example Usage

```text
Enter Youtube Url :
https://www.youtube.com/watch?v=VIDEO_ID

You : What project was built in this video?

AI : The video demonstrates building a React application...
```

---

## 📚 What I Learned

* Retrieval-Augmented Generation (RAG)
* Text Chunking Strategies
* Embedding Generation
* Vector Databases
* Semantic Search
* Context Augmentation
* LLM Integration with Ollama
* End-to-End RAG Pipeline Development

---

## 🔮 Future Improvements

* Streamlit Web Interface
* Source Citations
* Multi-Video Knowledge Base
* LangChain Integration
* LangGraph Workflows
* Agentic AI Features

---

## 👨‍💻 Author

Saarthak Pandey

GitHub: https://github.com/saarthakpandey03
LinkedIn: https://www.linkedin.com/in/saarthak-pandey-a24118330/
Portfolio: https://saarthakpandey.netlify.app/
# VideoMind-AI
