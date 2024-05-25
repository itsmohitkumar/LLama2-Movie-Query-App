import os
import torch
import warnings
import streamlit as st
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.embeddings.langchain import LangchainEmbedding
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.core import ServiceContext, set_global_service_context


# Load environment variables from .env file
load_dotenv()

# Ignore all warnings
warnings.filterwarnings("ignore")


# Configuration parameters for Llama2 model
name = os.getenv("LLAMA2_MODEL_NAME")
auth_token = os.getenv("LLAMA2_AUTH_TOKEN")

system_prompt = """<s> <<SYS>>
You are a helpful, respectful, and honest assistant. Always answer as
helpfully as possible while being safe. Your answers should not include
any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.
Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain
why instead of answering something not correct. If you don't know the answer
to a question, please don't share false information.

Your goal is to provide answers relating to movies and related information.<</SYS>>
"""
cache_dir = './model/'

# Configuration parameters for LLM
context_window = 128
max_new_tokens = 64
chunk_size = 128

@st.cache_resource
def get_tokenizer_model():
    try:
        tokenizer = AutoTokenizer.from_pretrained(name, cache_dir=cache_dir, use_auth_token=auth_token)
        model = AutoModelForCausalLM.from_pretrained(
            name, 
            cache_dir=cache_dir, 
            use_auth_token=auth_token, 
            torch_dtype=torch.float16, 
            rope_scaling={"type": "dynamic", "factor": 2}, 
            quantization_config=BitsAndBytesConfig()
        )
        return tokenizer, model
    except Exception as e:
        return None, None

tokenizer, model = get_tokenizer_model()
if tokenizer and model:
    llm = HuggingFaceLLM(
        context_window=context_window,
        max_new_tokens=max_new_tokens,
        system_prompt=system_prompt,
        model=model,
        tokenizer=tokenizer
    )

    embeddings = LangchainEmbedding(HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))

    service_context = ServiceContext.from_defaults(
        chunk_size=chunk_size,
        llm=llm,
        embed_model=embeddings
    )

    set_global_service_context(service_context)
else:
    raise Exception("Failed to initialize LLM. Check model setup.")
