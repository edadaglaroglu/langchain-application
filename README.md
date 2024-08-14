# 📄 Document Processing and Entity Extraction with LangChain and OpenAI GPT-4

Welcome to my project! This repository showcases how to harness the power of LangChain and OpenAI's GPT-4 to automate document processing and entity extraction. Below is a detailed overview of the project, including setup instructions, features, and more.

## 🚀 Project Overview

This project includes two main functionalities:

1. **📜 Document Summarization**: Automatically extracts specific information, such as individuals' favorite colors, from a series of documents.
2. **🔍 Entity Recognition & Storage**: Uses structured data models to identify and store entities like persons and cities from text input.

## 📂 Project Structure

- `document_processing.py`: The main script that processes documents and extracts entities.
- `README.md`: You're reading it! The project overview and setup guide.
- `requirements.txt`: Lists the Python dependencies needed for this project.

## ✨ Features

### 1. 📜 Document Summarization
- **Function**: `create_stuff_documents_chain`
- **Description**: Analyzes and summarizes documents, extracting relevant insights with ease.

### 2. 🔍 Entity Recognition & Storage
- **Function**: `create_openai_fn_runnable`
- **Description**: Maps natural language input to predefined data models, extracting and validating structured information.

## 🛠 Technologies Used

- **LangChain**: 🧠 A powerful framework for building and managing LLM chains.
- **OpenAI GPT-4**: 🤖 Provides advanced natural language processing capabilities.
- **Pydantic**: 📏 For defining and validating structured data models.

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8 or higher
- Required Python libraries: `langchain`, `openai`, `pydantic`

