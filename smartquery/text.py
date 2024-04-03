import click
import torch
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFacePipeline

# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    GenerationConfig,
    pipeline,
)
from smartquery.test1 import loader

def embeddings():
    EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceInstructEmbeddings(model_name=EMBEDDING_MODEL_NAME, model_kwargs={"device": 'cuda'})

    db = Chroma(
            persist_directory='/home/ubuntu/DB/',
            embedding_function=embeddings,
        )
    retriever = db.as_retriever(search_type = 'similarity', search_kwargs = {"k": 3})
    return retriever

def generate_text(query):

    #llm = load_model()

    qa = RetrievalQA.from_chain_type(llm=loader, chain_type="stuff", retriever=embeddings())

    #while True:
            #query = input("\nEnter a query: ")
            #if query == "exit":
            #    break
            # Get the answer from the chain
    res = qa(query)
    answer = res["result"]

            # Print the result
            #print("\n\n> Question:")
    print(query)
            #print("\n> Answer:")
    print(answer)
    return(answer)
