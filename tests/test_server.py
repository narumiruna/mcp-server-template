import pytest
from mcp import ClientSession
from mcp import StdioServerParameters
from mcp import stdio_client


@pytest.fixture
def server_params() -> StdioServerParameters:
    return StdioServerParameters(command="uv", args=["run", "mcpservertemplate"])


@pytest.asyncio
async def test_list_tools(server_params: StdioServerParameters) -> None:
    async with stdio_client(server_params) as (read, write), ClientSession(read, write) as session:
        result = await session.list_tools()
        assert len(result.tools) > 0
