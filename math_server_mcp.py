import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import AzureChatOpenAI  

load_dotenv()

async def run_agent():
    # Initialize MCP tool client
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["/Users/mohammadyawar/Desktop/MCP/math_server.py"],
                "transport": "stdio",
            }
        }
    )
    tools = await client.get_tools()

    # ✅ Azure OpenAI model initialization
    model = AzureChatOpenAI(
        temperature=0,
        azure_endpoint="https://oai-lexai-dev.openai.azure.com/",
        azure_deployment="gpt-4.1",  # <-- Your deployment name in Azure portal
        api_version="2025-01-01-preview",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Create ReAct agent
    agent = create_react_agent(
        model,
        tools,
        prompt="You are a mathetical tool to do complex aritmetic related problems",
    )

    # Run query
    agent_response = await agent.ainvoke({
        "messages": "what's (3 + 5) x 12?"
    })
    print(agent_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(run_agent())


