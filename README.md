# DeepSeek Chatbot with Ollama and LangChain

![Chatbot Demo](https://via.placeholder.com/800x400.png?text=Chatbot+Demo) <!-- Replace with actual screenshot -->

A fully functional, locally-run chatbot powered by **DeepSeek-R1 1.5B**, **Ollama**, and **LangChain**. This chatbot is designed for natural language conversations, code generation, and technical assistance. It features an attractive Streamlit-based front-end with chat history, avatars, and a modern UI.

---

## Features

- **Local LLM**: Runs entirely on your machine using Ollama and DeepSeek-R1 1.5B.
- **Chat History**: Maintains conversation history for context-aware responses.
- **Modern UI**: Beautifully designed chat interface with avatars and responsive layout.
- **Code Generation**: Specialized in software development and technical writing.
- **Customizable**: Easily modify prompts, avatars, and styling.

---

## Prerequisites

Before running the chatbot, ensure you have the following installed:

1. **Python 3.8+**
2. **Ollama** (for running the DeepSeek model locally)
3. **Streamlit** (for the web interface)
4. **LangChain** (for prompt management and chaining)

---

## Installation

1. **Install Ollama**:
   - Download and install Ollama from [here](https://ollama.ai/).
   - Pull the DeepSeek-R1 1.5B model:
     ```bash
     ollama pull deepseek-r1:1.5b
     ```

2. **Set Up Python Environment**:
   - Clone this repository:
     ```bash
     git clone https://github.com/shaikjr/deepseek-chatbot.git
     cd deepseek-chatbot
     ```
   - Install the required Python packages:
     ```bash
     pip install streamlit langchain-ollama
     ```

---

## Running the Chatbot

1. Start the Streamlit app:
   ```bash
   streamlit run chat.py
   
