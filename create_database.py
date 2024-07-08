from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, 'chroma')
DATA_PATH = os.path.join(BASE_DIR, 'data')

def main():
    print("Starting main function")
    generate_data_store()
    print("Completed data store generation")

def generate_data_store():
    print("Loading documents")
    documents = load_documents()
    print(f"Loaded {len(documents)} documents")
    
    print("Splitting text")
    chunks = split_text(documents)
    print(f"Split into {len(chunks)} chunks")
    
    print("Saving to Chroma")
    save_to_chroma(chunks)
    print("Saved chunks to Chroma")

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks")

    if len(chunks) > 10:
        document = chunks[10]
        print(document.page_content)
        print(document.metadata)
    else:
        print("Not enough chunks to display example")

    return chunks

def save_to_chroma(chunks: list[Document]):
    # Clear database
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    
    # Create new DB from docs
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH)
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}")

if __name__ == "__main__":
    main()
