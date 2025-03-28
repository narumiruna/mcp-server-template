from typing import Annotated

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Server Template")


@mcp.tool()
def add_numbers(
    a: Annotated[float, "The first number"],
    b: Annotated[float, "The second number"],
) -> str:
    """Add two numbers and return the result as a string."""
    return f"{a} + {b} = {a+b} from MCP Template"


def serve():
    mcp.run()
