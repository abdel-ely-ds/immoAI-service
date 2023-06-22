import os
from dotenv import load_dotenv
import pinecone

load_dotenv()


def init() -> None:
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV")
    )
