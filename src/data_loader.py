from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class MovieDataLoaderParser:
    def __init__(self,processed_csv):
        self.processed_csv = processed_csv

    def chunks(self):
        loader = CSVLoader(file_path=self.processed_csv,metadata_columns=[],encoding='utf-8')
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(separators=[""," ","  ","   ","\n","\n\n","\n\n\n"],chunk_size=1000,chunk_overlap=0)
        split_docs = splitter.split_documents(documents=docs)
        return split_docs        