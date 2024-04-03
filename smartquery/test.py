import logging

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

model_path = "/home/ubuntu/saved_model/"
tokenizer_path = "/home/ubuntu/saved_tokenizer/"

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path, use_fast=True)
    
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto",
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
        trust_remote_code=True,
        #max_memory={0: "15GB"},
        ).half()
    model.tie_weights()
    
    generation_config = GenerationConfig.from_pretrained("TheBloke/Wizard-Vicuna-7B-Uncensored-HF")
    
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.float16,
        max_length=2048,
        temperature=0.1,
        top_p=0.95,
        repetition_penalty=1.15,
        #device=0,
        generation_config=generation_config,
    )

    local_llm = HuggingFacePipeline(pipeline=pipe)
    
    return local_llm
