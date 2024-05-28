import os
import requests
import langchain
import streamlit as st

from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai.embeddings.azure import AzureOpenAIEmbeddings
from langchain_cohere import CohereEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import AzureOpenAI


OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2024-02-15-preview"
DEPLOYMENT_NAME = "nlp"

os.environ["OPENAI_API_TYPE"] = OPENAI_API_TYPE
os.environ["OPENAI_API_VERSION"] = OPENAI_API_VERSION
os.environ["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_API_KEY
os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT



def format_articles(data):
    formatted_text = ""
    for article in data['articles']:
        formatted_text += f"{article['title']}\n\n"
        if article['author']:
            formatted_text += f"Author: {article['author']}\n\n"
        formatted_text += f"{article['description']}\n\n"
        formatted_text += f"Published at: {article['publishedAt']}\n\n"
    return formatted_text


def main():
    st.title("Ask for News")

    API_KEY = "87836049190745a1b9b37da3fa0e4f03"
    url = "https://newsapi.org/v2/everything?q="  

    query="India"
    res = requests.get(f"{url}{query}&apiKey={API_KEY}")

    data = res.json()
    
    # Format the articles into a single string of text
    text = format_articles(data)
    raw_text = text


    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 800,
        chunk_overlap  = 200,
        length_function = len,
    )
    texts = text_splitter.split_text(raw_text)

    embeddings = CohereEmbeddings(cohere_api_key="3EN1jOQieMfDAuDupzFSGv8tfav1QXqvjitOFqZc")
    document_search = FAISS.from_texts(texts, embeddings)

    chain = load_qa_chain(AzureOpenAI(deployment_name=DEPLOYMENT_NAME,), chain_type="stuff")


    query = st.text_input('Ask question to the News website...')

    cancel_button = st.button('Cancel')

    if cancel_button:
        st.stop()

    if query:
      docs = document_search.similarity_search(query)


      next_query = "Please provide the category of news and then list the key details about it in bullet points, including any notable events, accusations, or developments:"
      _query=next_query + query


      st.write(chain.run(input_documents=docs, question=_query))

if __name__ == "__main__":
    main()
