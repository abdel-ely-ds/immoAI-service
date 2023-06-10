import json
import os
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Depends, Query
import pandas as pd
from langchain import OpenAI
from langchain.agents import create_pandas_dataframe_agent

from data_utils import read, pre_process, cols
from services.dashboard_service import DashboardService

app = FastAPI()
df: Optional[pd.DataFrame] = None
llm = None
agent = None


def _set_key():
    path = Path(".creds/.openai.json")
    with open(path) as f:
        creds = json.load(f)

    os.environ["OPENAI_API_KEY"] = creds["OPENAI_API_KEY"]


@app.on_event("startup")
async def startup_event():
    global df
    global llm
    global agent

    _set_key()
    df = read("immo_data.json")
    df = pre_process(df)[cols]
    llm = OpenAI(temperature=0)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)


@app.get("/")
def root():
    return {"message": "working"}


@app.get("/chat", status_code=200)
async def chat(
    question: str = Query(
        "What is the average price in oulfa district ? Give a response as a whole number",
        description="Ask any question about real estate market",
    )
):
    return agent.run(question.lower().strip())


@app.get("/dashboard", status_code=200)
async def get_dashboard(
    country: str = Query("Country3", description="Country you are interested in"),
    city: str = Query("City5", description="City you are interested in"),
    service: DashboardService = Depends(),
):
    return service.overview(df, country=country, city=city)
