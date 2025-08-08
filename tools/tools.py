from langchain.agents import Tool
from langchain_community.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv

load_dotenv(override=True)

serper = GoogleSerperAPIWrapper()
serper.run("What is the capital of France?")



tool_search =Tool(
        name="search",
        func=serper.run,
        description="Useful for when you need more information from an online search"
    )

tools = [tool_search]