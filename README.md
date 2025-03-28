# mcp-server-template

### GitHub

```json
{
  "mcpServers": {
    "mcp-server-template": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/narumiruna/mcp-server-template",
        "mcp-server-template"
      ]
    }
  }
}
```

### PyPI

```json
{
  "mcpServers": {
    "mcp-server-template": {
      "command": "uvx",
      "args": ["mcp-server-template"]
    }
  }
}
```

### Local

```json
{
  "mcpServers": {
    "mcp-server-template": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/home/<user>/workspace/mcp-server-template",
        "mcp-server-template"
      ]
    }
  }
}
```
