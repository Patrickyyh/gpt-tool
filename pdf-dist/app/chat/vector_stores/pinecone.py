import os
import pinecone
from langchain.vectorstores import Pinecone
from app.chat.embeddings.openai import embeddings

pinecone.init(
    api_key = os.getenv("PINECONE_API_KEY"),
    environment = os.getenv("PINECONE_ENV_NAME")
)
vectorstore = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"),
    embeddings
)
def build_retriever(chat_args):
    ## define the search_kwargs:
    ## We would like to filter out the the document belongs to
    ## the specific pdf over here
    search_kwargs = {"filter" : {"pdf_id":chat_args.pdf_id}}
    return vectorstore.as_retriever(search_kwargs = search_kwargs)







