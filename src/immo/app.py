from typing import Optional

import pandas as pd
from fastapi import Depends, FastAPI, Query
from langchain import OpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent import AgentExecutor
from langchain.memory import ConversationBufferMemory
from fastapi.middleware.cors import CORSMiddleware

from immo import data_utils as du
from immo import keys
from immo import tools
from immo.services.dashboard_service import DashboardService
import os

app = FastAPI()
df: Optional[pd.DataFrame] = None
agent: Optional[AgentExecutor] = None
memory = ConversationBufferMemory(memory_key="chat_history")

cols = ["price", "rooms", "surface", "city", "district", "description"]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    global df
    global agent

    keys.set_openai()
    keys.set_pinecone()

    df = du.read(os.path.abspath("data/immo_data.json"))
    df = du.pre_process(df)[cols]
    llm = OpenAI(temperature=0)

    agent = initialize_agent(
        agent="conversational-react-description",
        tools=tools.load(llm, df),
        llm=llm,
        verbose=True,
        max_iterations=3,
        memory=memory,
    )


@app.get("/")
def root():
    return {"message": "working"}


@app.get("/immo", status_code=200)
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