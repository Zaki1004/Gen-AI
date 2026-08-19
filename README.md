<div align="center">

# ☕ CoffeeBot

### AI-Powered Coffee Shop Assistant with LangGraph, RAG & SQL Agent

CoffeeBot is an intelligent coffee shop assistant built using **LangGraph**, **LangChain**, **Retrieval-Augmented Generation (RAG)**, **FAISS**, **SQLite**, and **Groq LLM**. It helps users learn about coffee, receive menu recommendations, place orders, and simulate payments through a conversational interface.

---

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-AI-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent-orange)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-purple)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success)

</div>

---

# 📖 Overview

CoffeeBot is an AI-powered chatbot designed to simulate an intelligent coffee shop assistant.

Unlike a traditional chatbot, CoffeeBot combines multiple AI techniques including **Retrieval-Augmented Generation (RAG)**, **tool calling**, and **LangGraph agent orchestration** to provide context-aware and accurate responses.

The assistant is capable of:

- Answering coffee-related questions using a knowledge base.
- Retrieving relevant information from PDF documents with RAG.
- Querying a SQLite database to recommend menu items.
- Managing customer orders and shopping carts.
- Simulating payment and order history.
- Delivering responses through a modern ChatGPT-inspired interface.

The project was developed as a practical implementation of modern Generative AI technologies while maintaining a clean software architecture and modular codebase.

---

# ✨ Features

## 🤖 AI Assistant

- Natural language conversation
- Context-aware responses
- Multi-turn conversation
- ChatGPT-inspired interface
- Typing animation
- Responsive UI

---

## 📚 Retrieval-Augmented Generation (RAG)

- PDF Knowledge Base
- Semantic Search
- FAISS Vector Store
- Sentence Transformer Embedding
- Query Expansion
- Context Retrieval

---

## 🧠 LangGraph Agent

CoffeeBot uses LangGraph to determine which tool should be executed depending on the user's request.

Current agent capabilities include:

- Coffee Knowledge Retrieval
- SQL Query Tool
- Order Detection
- Cart Management
- Payment Flow
- General Conversation

---

## 🗄 SQL Tool

The SQL Tool enables CoffeeBot to interact directly with the SQLite database.

Examples:

- Recommend coffee menu
- Cheapest menu
- Most expensive drink
- Available snacks
- Heavy meals
- Menu price lookup
- Category filtering

---

## 🛒 Order Management

CoffeeBot supports an end-to-end ordering simulation.

Features include:

- Add item to cart
- Quantity management
- Cart summary
- Checkout
- Payment simulation
- Order history

---

## 🎨 User Experience

- Modern chat interface
- Responsive layout
- Coffee-inspired color palette
- Popover cart
- Popover history
- Empty state illustration
- Streaming typing effect

---

## 🐳 Deployment Ready

CoffeeBot is containerized using Docker.

Supported environments:

- Local Development
- Docker Desktop
- Docker Compose

---

# 🛠 Tech Stack

## Programming Language

- Python

---

## Frontend

- Streamlit

---

## AI Framework

- LangChain
- LangGraph

---

## Large Language Model

- Groq API

---

## Retrieval-Augmented Generation

- FAISS
- Sentence Transformers

---

## Database

- SQLite

---

## Knowledge Base

- PDF Documents

---

## Containerization

- Docker
- Docker Compose

---

## Development Tools

- VS Code
- Git
- GitHub
- Miniconda

---

# 🎯 Project Goals

The primary objective of CoffeeBot is to demonstrate how multiple Generative AI technologies can be integrated into a single intelligent application.

Instead of relying solely on an LLM, CoffeeBot combines:

- Knowledge Retrieval (RAG)
- Database Query (SQL)
- Agent Orchestration (LangGraph)
- Tool Calling
- Modular Architecture

This architecture enables CoffeeBot to produce responses that are more reliable, explainable, and scalable than a standard conversational chatbot.

# 🏗 System Architecture

CoffeeBot follows a modular architecture that separates the user interface, AI orchestration, retrieval pipeline, database operations, and business logic.

```text

                 CoffeeBot AI System

                       USER
                         │
                         ▼
                Streamlit Interface
                         │
                         ▼
                LangGraph Agent
      ┌──────────┼────────────┬──────────┐
      ▼          ▼            ▼          ▼
  SQL Tool   RAG Tool    Order Tool   LLM Chat
      │          │            │
      ▼          ▼            ▼
 SQLite DB   FAISS      Cart Service
                 │            │
                 ▼            ▼
            Knowledge     Payment
               PDF           │
                             ▼
                        Order History

               ─────────────────────

                    Groq LLM
                        │
                        ▼
                 Final Response
```

---

# 🔄 Application Workflow

The overall workflow of CoffeeBot can be summarized as follows.

```text
User Question

      │

      ▼

Streamlit UI

      │

      ▼

LangGraph Agent

      │

      ├────────────── Coffee Knowledge?
      │                     │
      │                     ▼
      │               RAG Pipeline
      │
      ├────────────── Menu Recommendation?
      │                     │
      │                     ▼
      │                 SQL Tool
      │
      ├────────────── Order?
      │                     │
      │                     ▼
      │              Cart Service
      │
      ├────────────── Payment?
      │                     │
      │                     ▼
      │            Payment Service
      │
      ▼

Groq LLM

      │

      ▼

Response Rendering

      │

      ▼

User
```

# 🧠 LangGraph Agent Flow

CoffeeBot uses **LangGraph** as the central orchestration engine.

Instead of sending every prompt directly to the LLM, the agent first analyzes the user's intent and determines which tool should be executed.

```text

                         User Prompt
                              │
                              ▼
                     LangGraph Coffee Agent
                              │
     ┌──────────────┬──────────────┬──────────────┐
     │              │              │              │
     ▼              ▼              ▼              ▼
 SQL Tool      RAG Tool      Order Tool    General Chat
     │              │              │
     ▼              ▼              ▼
 SQLite DB      Retriever     Cart Service
                    │              │
                    ▼              ▼
               FAISS Index    Order Service
                    │              │
                    ▼              ▼
              Knowledge PDF    Payment Service
     └──────────────┴──────────────┘
                    │
                    ▼
                 Groq LLM
                    │
                    ▼
              Final Response
```

The LangGraph agent acts as the decision-making layer of CoffeeBot. It analyzes the user's intent and routes the request to the appropriate tool before sending the enriched context to the Groq Large Language Model.

This architecture enables CoffeeBot to:

- Retrieve coffee knowledge using RAG.
- Query menu information directly from SQLite.
- Process customer orders and cart operations.
- Handle general conversations without external tools.

## As a result, CoffeeBot provides responses that are more accurate, contextual, and efficient than relying solely on an LLM.

# 📚 Retrieval-Augmented Generation (RAG) Pipeline

CoffeeBot uses Retrieval-Augmented Generation (RAG) to answer coffee-related questions based on its knowledge base.

The retrieval pipeline works as follows:

```text
PDF Knowledge

      │

      ▼

Document Loader

      │

      ▼

Text Splitter

      │

      ▼

Sentence Transformer

      │

      ▼

Embedding Vector

      │

      ▼

FAISS Index

============================

User Question

      │

      ▼

Query Expansion

      │

      ▼

Sentence Embedding

      │

      ▼

Similarity Search

      │

      ▼

Top-K Chunks

      │

      ▼

Groq LLM

      │

      ▼

Answer
```

> **Note:** Embeddings are generated only during the indexing process. During runtime, CoffeeBot loads the existing FAISS index (`coffeebot.index`) and document chunks (`chunks.pkl`), ensuring faster startup and retrieval.

---

# 🗄 SQL Query Pipeline

For menu-related questions, CoffeeBot retrieves live data directly from the SQLite database.

```text
User Request

      │

      ▼

LangGraph Agent

      │

      ▼

SQL Tool

      │

      ▼

SQLite Database

      │

      ▼

Query Result

      │

      ▼

Groq LLM

      │

      ▼

Natural Language Response
```

This enables CoffeeBot to provide accurate and up-to-date information about menu items, categories, prices, and recommendations.

---

# 🛒 Ordering Workflow

CoffeeBot supports an end-to-end ordering simulation.

```text
User

      │

      ▼

Place Order

      │

      ▼

Order Detection

      │

      ▼

Cart Service

      │

      ▼

Shopping Cart

      │

      ▼

Checkout

      │

      ▼

Payment Service

      │

      ▼

Order History

      │

      ▼

Completed Order
```

---

# 📂 Project Structure

```text
CoffeeBot/
│
├── agents/                # LangGraph agent orchestration
├── config/                # Application configuration
├── database/              # SQLite database
├── knowledge/             # Coffee knowledge PDFs
├── rag/                   # Retrieval-Augmented Generation
├── services/              # Business logic & services
├── tests/                 # Testing files
├── tools/                 # LangGraph tools
├── ui/                    # Streamlit UI components
├── utils/                 # Utility functions
├── vectorstore/           # FAISS index & document chunks
│
├── app.py                 # Streamlit entry point
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 🧩 Project Design Principles

CoffeeBot was designed with the following principles:

- **Modular Architecture** – Separate UI, services, RAG, tools, and agent logic.
- **Single Responsibility Principle** – Each module has one clear responsibility.
- **Agent-Based Workflow** – LangGraph determines which tool to execute.
- **Retrieval Before Generation** – Use RAG and SQL retrieval before generating responses.
- **Production-Oriented Structure** – Dockerized, organized folders, and reusable components.
- **Scalable Design** – Easy to extend with new tools, knowledge sources, or features.

# 🚀 Getting Started

Follow the instructions below to run CoffeeBot locally or using Docker.

---

# 📋 Prerequisites

Before running CoffeeBot, make sure the following software is installed on your machine.

## Development Environment

- Python 3.12+
- Miniconda or Anaconda
- Git
- Visual Studio Code

---

## Deployment Environment

- Docker Desktop
- Docker Compose

---

# 📥 Clone Repository

```bash
git clone https://github.com/Zaki1004/Gen-AI.git
```

---

# 🐍 Local Development Setup

## Create Conda Environment

```bash
conda create -n (project-name) python=3.12
```

---

## Activate Environment

```bash
conda activate (project-name)
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

CoffeeBot uses environment variables to securely store sensitive credentials.

1. Create a `.env` file in the project root.
2. Copy the contents from `.env.example`.
3. Replace the placeholder value with your own Groq API Key.

Example:

```env
Groq_API_KEY=<YOUR_Groq_API_KEY>
```

> **Note:** Never commit your `.env` file or expose your API keys publicly. The `.env` file is ignored by Git via `.gitignore`.

## Run CoffeeBot

```bash
streamlit run app.py
```

CoffeeBot will be available at

```
http://localhost:8501
```

---

# 🐳 Run with Docker

CoffeeBot also supports Docker for a consistent runtime environment.

---

## Build Docker Image

```bash
docker compose build
```

---

## Run CoffeeBot

```bash
docker compose up
```

or

```bash
docker compose up --build
```

if the Docker image needs to be rebuilt.

---

CoffeeBot will be available at

```
http://localhost:8501
```

---

## Stop Container

```bash
docker compose down
```

---

# ⚙ Environment Variables

CoffeeBot currently uses the following environment variables.

| Variable       | Description                       |
| -------------- | --------------------------------- |
| Groq_API_KEY | API Key used to access Groq LLM |

Example

```env
Groq_API_KEY=YOUR_API_KEY
```

---

# 📁 Knowledge Base

CoffeeBot uses PDF documents as its knowledge source.

```
knowledge/
```

These documents are processed into embeddings and stored inside

```
vectorstore/
```

```
vectorstore/
├── coffeebot.index
└── chunks.pkl
```

During runtime, CoffeeBot loads the existing FAISS index instead of rebuilding embeddings, resulting in significantly faster startup times.

---

# 💬 Example Questions

Users can ask questions such as:

### Coffee Knowledge

- What is Arabica coffee?
- Explain the coffee roasting process.
- What is the difference between espresso and americano?

---

### Menu Recommendation

- Recommend a sweet coffee.
- What is the cheapest coffee?
- Show me all non-coffee drinks.
- Which menu has the highest price?

---

### Ordering

- I want one Cappuccino.
- Add two Croissants.
- Checkout my order.
- Show my cart.

---

### General Conversation

- Hello CoffeeBot.
- What can you do?
- Tell me today's recommendation.

---

# 🧪 Testing

Before pushing new changes, ensure the following features work correctly.

## AI

- Chat Conversation
- RAG Retrieval
- SQL Tool
- LangGraph Agent

---

## Business

- Add to Cart
- Checkout
- Payment
- Order History

---

## UI

- Responsive Layout
- Chat Interface
- Cart Popover
- History Popover

---

## Docker

```bash
docker compose build

docker compose up
```

Verify that CoffeeBot runs successfully inside Docker before deployment.

---

# 🚀 Future Improvements

The current version of CoffeeBot focuses on demonstrating an intelligent AI-powered coffee shop assistant.

Future improvements may include:

- User Authentication
- Customer Profiles
- Real-Time Order Tracking
- Admin Dashboard
- Recommendation Personalization
- Multi-language Support
- Online Payment Gateway
- Mobile Application
- Cloud Deployment
- Analytics Dashboard

---

# 👨‍💻 Author

**Zaki Waliyan Isnanto**

Information Technology Graduate

Frontend Engineer | AI Enthusiast

GitHub:
https://github.com/Zaki1004

LinkedIn:
https://www.linkedin.com/in/zaki10/

---

# 📄 License

This project was developed for educational purposes and as a personal portfolio project.

Feel free to explore, learn from, and improve the project.

© 2026 Zaki Waliyan Isnanto
