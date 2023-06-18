import json
import os
from pathlib import Path

import pinecone


def set_openai() -> None:
    path = Path(os.path.abspath(".creds/.openai.json"))
    with open(path) as f:
        creds = json.load(f)

    os.environ["OPENAI_API_KEY"] = creds["OPENAI_API_KEY"]


def set_pinecone() -> None:
    path = Path(os.path.abspath(".creds/.pinecone.json"))
    with open(path) as f:
        creds = json.load(f)

    pinecone.init(api_key=creds["PINECONE_API_KEY"], environment=creds["PINECONE_ENV"])
