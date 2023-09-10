
# Streamlit Chatbot powered by LlamaIndex

## Overview

This application is a chatbot built with Streamlit and LlamaIndex. It serves as an interface for asking questions related to documents. The underlying engine uses OpenAI's GPT-4 model for generating responses.

## Features

- **Interactive UI**: Ask questions through a chat input and view responses in real time.
- **Document Indexing**: Uses the LlamaIndex library for indexing documents for the chat.
- **Powered by GPT-4**: Utilizes OpenAI's GPT-4 model for generating responses.

## Dependencies

- Streamlit
- LlamaIndex
- OpenAI

## How to Run

1. Set your OpenAI API key in Streamlit's `st.secrets`.
2. Run `streamlit run app.py` in your terminal.

## Code Explanation

- Initializes Streamlit and sets API key for OpenAI.
- Loads and indexes documents from a directory.
- Manages chat history and session state.
- Utilizes LlamaIndex's chat engine for generating responses based on the indexed documents.

## Author

Your Name

## License

This project is licensed under the MIT License.

