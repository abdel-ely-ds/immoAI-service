from typing import List

import pandas as pd
from langchain.agents import create_pandas_dataframe_agent, load_tools
from langchain.llms import BaseLLM
from langchain.tools import Tool


def create_pandas_tool(llm: BaseLLM, df: pd.DataFrame) -> Tool:
    pandas_agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    return Tool(
        name="Pandas",
        func=pandas_agent.run,
        description="Useful for when you need to answer questions about typical, average, min, max prices"
        "number of properties, typical property in a city/district",
    )


def load(llm: BaseLLM, df: pd.DataFrame) -> List[Tool]:
    tools = load_tools(["llm-math"], llm=llm)

    to_add = [create_pandas_tool(llm, df)]
    tools.extend(to_add)
    return tools
