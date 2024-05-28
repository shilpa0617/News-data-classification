# Rag-Based LLM Chatbot for News Query
This project is a Rag-based LLM (Language Model) chatbot designed to provide users with news articles based on their queries. The chatbot utilizes the News API to fetch news articles related to a given topic and presents them to the user in a conversational format. The user can ask questions about the news articles, and the chatbot will provide relevant answers using a pre-trained language model.

## Installation

1. Clone the repository. 
2. cd into your directory/ open with vscode
3. Create a Virtual Environment: `python -m venv env`
4. Run the virtual environment: `source env/bin/activate` - for MacOS, `env/Scripts/activate` - for Linux, `env/Scripts/activate.bat` - for Windows cmd, `env/Scripts/Activate.ps1` - for Windows PowerShell 
5. Install the required dependencies: `pip install -r requirements.txt`
6. Generate an OpenAI API Key and include it in your .env file along with setting up environment variables for the News API key.
7. Run the application: `streamlit run app.py`

In case you're facing "PermissionError: [WinError 10013] An attempt was made to access a socket in a way forbidden by its access permissions" on Windows try to run following commands in elevated PowerShell 
- `net stop hns`
- `net start hns`

## Technologies Used
+ **Python:** The primary programming language used for developing the chatbot.
+ **Streamlit:** The web application framework used for building the user interface.
+ **Requests:** The library used for making HTTP requests to the News API.
+ **Langchain:** The library used for text processing and embedding.
+ **OpenAI:** The API used for question answering tasks.
