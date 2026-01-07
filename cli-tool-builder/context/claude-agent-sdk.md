# Claude Agent SDK for Intelligent Features

When a CLI tool requires "intelligence" or needs to handle unreliable data sources, use the Claude Agent SDK to add agentic capabilities.

## When to Use

- **Data gathering from unreliable sources**: APIs that might fail or change
- **Intelligent processing**: Tasks requiring reasoning or judgment
- **Web search fallback**: When structured APIs don't exist
- **File operations**: Reading, writing, and analyzing files
- **Complex workflows**: Multi-step tasks requiring tool use

## Dependencies

Use inline script metadata (PEP 723) to declare the dependency:

```python
# /// script
# dependencies = ["claude-agent-sdk", "anyio"]
# ///
```

Then run with `uv run script.py`.

## Basic Usage: query()

The simplest way to use the SDK - async streaming responses:

```python
# /// script
# dependencies = ["claude-agent-sdk", "anyio"]
# ///

import anyio
from claude_agent_sdk import query, AssistantMessage, TextBlock

async def ask_claude(prompt: str) -> str:
    """Simple query to Claude."""
    result = []
    async for message in query(prompt=prompt):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    result.append(block.text)
    return "".join(result)

async def main():
    response = await ask_claude("What is 2 + 2?")
    print(response)

anyio.run(main)
```

## With Options

Configure behavior with `ClaudeAgentOptions`:

```python
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    system_prompt="You are a helpful data extraction assistant",
    max_turns=3,
    cwd="/path/to/project"  # Working directory
)

async for message in query(prompt="Extract the revenue figures", options=options):
    print(message)
```

## Using Built-in Tools

Enable Claude to use tools like file operations and bash:

```python
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write", "Bash"],
    permission_mode='acceptEdits'  # Auto-accept file edits
)

async for message in query(
    prompt="Read config.json and extract the API endpoint",
    options=options
):
    print(message)
```

## Creating Custom Tools

Define your own tools as in-process MCP servers:

```python
from claude_agent_sdk import (
    tool, 
    create_sdk_mcp_server, 
    ClaudeAgentOptions, 
    ClaudeSDKClient
)

@tool("fetch_stock_price", "Fetch current stock price", {"symbol": str})
async def fetch_stock_price(args):
    symbol = args["symbol"]
    # Your implementation here
    price = get_price_from_api(symbol)
    return {
        "content": [
            {"type": "text", "text": f"${price}"}
        ]
    }

server = create_sdk_mcp_server(
    name="financial-tools",
    version="1.0.0",
    tools=[fetch_stock_price]
)

options = ClaudeAgentOptions(
    mcp_servers={"finance": server},
    allowed_tools=["mcp__finance__fetch_stock_price"]
)

async with ClaudeSDKClient(options=options) as client:
    await client.query("What's the current price of AAPL?")
    async for msg in client.receive_response():
        print(msg)
```

## Interactive Conversations with ClaudeSDKClient

For multi-turn conversations:

```python
from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient

options = ClaudeAgentOptions(
    allowed_tools=["Read", "Bash"],
    system_prompt="You help users analyze data files"
)

async with ClaudeSDKClient(options=options) as client:
    # First query
    await client.query("List all CSV files in the current directory")
    async for msg in client.receive_response():
        print(msg)
    
    # Follow-up query (maintains context)
    await client.query("Analyze the first one and summarize the data")
    async for msg in client.receive_response():
        print(msg)
```

## Error Handling

```python
from claude_agent_sdk import (
    query,
    CLINotFoundError,
    ProcessError,
    CLIJSONDecodeError,
)

try:
    async for message in query(prompt="Hello"):
        print(message)
except CLINotFoundError:
    print("Claude Agent SDK CLI not found")
except ProcessError as e:
    print(f"Process failed with exit code: {e.exit_code}")
except CLIJSONDecodeError as e:
    print(f"Failed to parse response: {e}")
```

## Fallback Strategy

When designing CLI tools, use this hierarchy:

1. **Direct API** - Use official APIs when available and reliable
2. **Structured scraping** - Parse web pages if no API exists
3. **Claude Agent SDK** - For dynamic, complex, or unreliable data needs

## Example: Financial Data with Fallback

```python
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock

async def get_financial_data(company: str, metric: str) -> str:
    """Get financial data with fallback to Claude Agent."""
    
    # Try direct API first
    try:
        return query_financial_api(company, metric)
    except APIError:
        pass
    
    # Fallback to Claude Agent with file reading capability
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Bash"],
        system_prompt="Extract financial metrics accurately. Return just the number with units."
    )
    
    result = []
    async for message in query(
        prompt=f"Find the {metric} for {company} from their most recent SEC filing.",
        options=options
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    result.append(block.text)
    
    return "".join(result)
```

## Key Principles

1. **Prefer deterministic solutions** when they work reliably
2. **Use Claude Agent for complex tasks** requiring reasoning or tool use
3. **Enable appropriate tools** for the task at hand
4. **Structure prompts clearly** for consistent outputs
5. **Handle failures gracefully** with proper error handling
