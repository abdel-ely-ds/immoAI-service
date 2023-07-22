import os

import pinecone
from dotenv import load_dotenv

load_dotenv()


def init() -> None:
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV")
    )
