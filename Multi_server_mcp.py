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
            },


            "bright_data": {
                "command": "npx",
                "args": ["@brightdata/mcp"],
                "env": { "API_TOKEN": os.getenv("BRIGHT_DATA_API_TOKEN"),
                },
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

    prompt = """
    You are a smart assistant with two tools:
    1. Math tool to solve arithmetic or numeric problems.
    2. BrightData tool to search the web and get the latest information.

    Use the right tool based on the question and give clear, correct answers.
    """

    # Create ReAct agent
    agent = create_react_agent(
        model,
        tools,
        prompt=prompt
    )

    # Run query
    agent_response = await agent.ainvoke({
        "messages": "who won the IPL 2025"
    })
    print(agent_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(run_agent())
