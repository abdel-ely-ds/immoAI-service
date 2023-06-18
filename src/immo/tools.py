from typing import List

import pandas as pd
import pinecone
from langchain.agents import create_pandas_dataframe_agent, load_tools
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import BaseLLM
from langchain.tools import Tool
from langchain.vectorstores import Pinecone


def _load_vector_store(index_name: str, embed, text_field: str = "text") -> Pinecone:
    index = pinecone.Index(index_name)
    return Pinecone(index, embed.embed_query, text_field)


def create_pandas_tool(llm: BaseLLM, df: pd.DataFrame) -> Tool:
    pandas_agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    return Tool(
        name="Pandas",
        func=pandas_agent.run,
        description="Useful for when you need to answer questions about typical, average, min, max prices"
        "number of properties, typical property in a city/district",
    )


def create_similarity_tool(vector_store: Pinecone) -> Tool:
    return Tool(
        name="Similarity",
        func=vector_store.similarity_search,
        description="Useful for when you need to find similar properties",
    )


def load(
    llm: BaseLLM,
    df: pd.DataFrame,
    index_name: str = "langchain-bot",
    text_field: str = "text",
) -> List[Tool]:
    tools = load_tools(["llm-math"], llm=llm)
    vector_store = _load_vector_store(index_name, OpenAIEmbeddings(), text_field)

    to_add = [create_pandas_tool(llm, df), create_similarity_tool(vector_store)]
    tools.extend(to_add)
    return tools
