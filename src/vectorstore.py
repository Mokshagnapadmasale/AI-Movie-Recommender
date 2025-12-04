from langchain_community.vectorstores import Chroma
from config.config import OPENAI_API_KEY,OPENAI_EMBEDDING_MODEL_NAME
from huggingface_hub import InferenceClient
from langchain_openai.embeddings import OpenAIEmbeddings

class VectorStore:

    def __init__(self,docs,persist_directory):
        self.docs = docs
        self.persist_directory = persist_directory
        self.embedding = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL_NAME,api_key=OPENAI_API_KEY)


    def load_docs(self):
        vectorstore = Chroma(embedding_function=self.embedding,collection_name='chroma_db',persist_directory=self.persist_directory)
        db = vectorstore.as_retriever(search_type='mmr',search_kwargs={'k':5})
        return db

    def save_docs(self):
        vectorstore = Chroma.from_documents(collection_name='chorma_db',documents=self.docs,persist_directory=self.persist_directory,embedding=self.embedding)
        db = vectorstore.as_retriever(search_type='mmr',search_kwargs={'k':5})
        return db 