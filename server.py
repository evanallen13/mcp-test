from mcp.server.fastmcp import FastMCP
import subprocess
import time

mcp = FastMCP("evan-devops-mcp")

@mcp.tool()
def ping_ip(ip: str) -> dict:
    """
    Ping an IP address and return latency in milliseconds.
    """
    start = time.time()

    try:
        subprocess.check_output(
            ["ping", "-c", "1", ip],
            stderr=subprocess.STDOUT
        )

        latency = (time.time() - start) * 1000

        return {
            "ip": ip,
            "latency_ms": round(latency, 2),
            "status": "reachable"
        }

    except subprocess.CalledProcessError:
        return {
            "ip": ip,
            "status": "unreachable"
        }


@mcp.tool()
def hello(name: str) -> str:
    """
    Simple hello world tool
    """
    return f"Hello {name}! MCP server is working!!!"


# Start server
if __name__ == "__main__":
    mcp.run()