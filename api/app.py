from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()



app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)


##ollama llama3.2
llm=Ollama(model="llama3.2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")


add_routes(
    app,
    prompt1|llm,
    path="/essay"


)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
