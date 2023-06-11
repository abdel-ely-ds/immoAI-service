import json
import os
from pathlib import Path


def export() -> None:
    path = Path(".creds/.openai.json")
    with open(path) as f:
        creds = json.load(f)

    os.environ["OPENAI_API_KEY"] = creds["OPENAI_API_KEY"]
