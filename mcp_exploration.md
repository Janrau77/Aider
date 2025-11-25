# Exploring the Model Context Protocol (MCP)

## 1. Objective

This project aims to understand the Model Context Protocol (MCP), its core concepts, its importance in the field of AI agents, and what practical applications can be built with it.

## 2. What is MCP? (Initial Understanding)

MCP is an open standard designed to be a "universal connector" for AI models. It standardizes how AI agents, especially LLMs, communicate and interact with external tools, APIs, and data sources. The goal is to solve the problem of creating custom integrations for every new tool an agent needs to use.

## 3. Core Concepts to Investigate

Based on initial research, the key components of an MCP setup are:

*   **MCP Host:** The main AI application or agent environment.
*   **MCP Client:** An intermediary that runs within the Host.
*   **MCP Server:** The component that exposes a specific tool or data source for the agent to use.

## 4. Learning Plan & Next Steps

Here is our step-by-step plan to learn about MCP:

- [x] **Step 1: Find Official Resources:** Locate the official MCP specification, whitepaper, or primary website to get information from the source.
  - The official website is: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
- [x] **Step 2: Find Implementations:** Search for open-source frameworks or libraries that implement the MCP standard (e.g., `mcp-agent`).
  - Anthropic provides official SDKs (Python, TypeScript, etc.) and a repository of reference server implementations.
  - The official GitHub repository is: [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- [x] **Step 3: Discover Tutorials & Examples:** Look for beginner-friendly tutorials, code examples, or articles that demonstrate a simple MCP setup in action.
  - Found a beginner-friendly tutorial for the Python SDK.
  - **Example Project:** A simple calculator server that exposes `add`, `subtract`, `multiply`, and `divide` functions as "tools" that an AI agent can use.
  - **Code (`calculator_server.py`):**
    ```python
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
    ```
- [ ] **Step 4: Brainstorm a Project:** Based on our findings, design a small, practical project we could potentially build to solidify our understanding.
