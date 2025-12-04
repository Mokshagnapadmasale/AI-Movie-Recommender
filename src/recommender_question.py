from langchain_core.runnables import RunnableMap,RunnableLambda
from src.prompt_template import get_template
from langchain_groq.chat_models import ChatGroq
from config.config import GROQ_MODEL_NAME,GROQ_API_KEY
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

class RecommenderAnswer:
    def __init__(self,retriver):
        self.prompt_template = get_template()
        self.llm = ChatGroq(model=GROQ_MODEL_NAME,api_key=GROQ_API_KEY)
        self.retriver = retriver

    def recommender(self,question:str):
        document_chain = create_stuff_documents_chain(llm=self.llm,prompt=self.prompt_template)
        chain = RunnableMap(
            {
                'input' : RunnableLambda(lambda x : x['input']),
                'context' : RunnableLambda(lambda x : self.retriver.invoke(x['input']))
            }
        ) | document_chain | RunnableLambda(lambda x : {'output':x})
        response = chain.invoke({'input':question})
        result = response['output']
        return result.strip()