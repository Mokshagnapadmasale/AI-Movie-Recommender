from pipelines.build_pipeline import build_pipeline
import streamlit as st 


st.set_page_config(page_title='AI-Movie-Recommender',layout='centered')
st.header(body='Movie-Recommender',divider="rainbow")

question = st.text_input(label='prompt Here')
if question:
    result = build_pipeline(persist_directory=r'C:\Users\moksh\Desktop\ENDTOEND\Movie-Recomender\data',question=question)
    st.markdown(result)