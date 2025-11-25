from mcp.server.fastmcp import FastMCP
from typing import Union

# Initialize an MCP server instance with a descriptive name
mcp = FastMCP("Calculator Server")

@mcp.tool("add")
def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers together.
    :param a: The first number.
    :param b: The second number.
    :return: The sum of a and b.
    """
    return a + b

@mcp.tool("subtract")
def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts the second number from the first.
    :param a: The first number.
    :param b: The second number.
    :return: The difference between a and b.
    """
    return a - b

@mcp.tool("multiply")
def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies two numbers.
    :param a: The first number.
    :param b: The second number.
    :return: The product of a and b.
    """
    return a * b

@mcp.tool("divide")
def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divides the first number by the second.
    :param a: The first number (dividend).
    :param b: The second number (divisor).
    :return: The quotient of a and b.
    :raises ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    mcp.run()
