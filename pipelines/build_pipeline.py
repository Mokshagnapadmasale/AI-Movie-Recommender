from src.data_loader import MovieDataLoaderParser
from src.recommender_question import RecommenderAnswer
from src.vectorstore import VectorStore
from src.data_processor import MovieDataProcessor
import os
from pathlib import Path

def build_pipeline(persist_directory,question:str):
    processed_csv = MovieDataProcessor(original_csv=r'C:\Users\moksh\Desktop\ENDTOEND\Movie-Recomender\data\tmdb_freeplan_movies_final.csv',processed_csv=r'C:\Users\moksh\Desktop\ENDTOEND\Movie-Recomender\data\final.csv').load_process_movie_data()
    loader = MovieDataLoaderParser(processed_csv=processed_csv)
    docs = loader.chunks()
    vc  = VectorStore(docs=docs,persist_directory=persist_directory)
    if os.path.exists(persist_directory):
        retriever = vc.load_docs()
    else:
        retriever = vc.save_docs()
    recommender = RecommenderAnswer(retriver=retriever)
    answer = recommender.recommender(question=question)
    return answer