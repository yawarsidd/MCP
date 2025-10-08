import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import AzureChatOpenAI  


load_dotenv()

async def run_agent():

    client = MultiServerMCPClient(
        {
            "bright_data": {
                "command": "npx",
                "args": ["@brightdata/mcp"],
                "env": {
                    "API_TOKEN": os.getenv("BRIGHT_DATA_API_TOKEN"),
                },
                "transport": "stdio",
            },
        }
    )
    tools = await client.get_tools()
    model = AzureChatOpenAI(
        temperature=0,
        azure_endpoint="https://oai-lexai-dev.openai.azure.com/",
        azure_deployment="gpt-4.1",  
        api_version="2025-01-01-preview",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    agent = create_react_agent(model, tools, prompt="You are a web search agent with access to brightdata tool to get latest data")
    agent_response = await agent.ainvoke({"messages": "Who won IPL 2025"})
    print(agent_response["messages"][-1].content)

# Tell me available flights from Bangalore to Delhi on Dec 1 2025

if __name__ == "__main__":
    asyncio.run(run_agent())