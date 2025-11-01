# MCP Project Setup

## Project Overview
This project is an MCP (Model Context Protocol) tool server for searching and processing RSS feeds. It provides programmable tools for querying news articles and YouTube videos using RSS, designed to be compatible with MCP inspector and automation workflows. The codebase is structured for easy extension and integration with other MCP-compatible systems.

## How to run

1. **Activate your virtual environment** (Windows):
   ```powershell
   .venv\Scripts\activate
   ```
2. **Run your MCP tool:**
   ```powershell
   python src\feed_mcp.py
   ```

- You only need to activate the environment once per terminal session.
- All Python commands in that terminal will use the virtual environment until you close the terminal or run `deactivate`.

## Extra: Inspector usage
If you want to use the Model Context Protocol inspector:
```powershell
npx @modelcontextprotocol/inspector python src\feed_mcp.py
```

## Requirements
- Python 3.12+
- Packages: fastmcp, feedparser (install with `python -m pip install -r requirements.txt`)

## Virtual environment creation (if not present)
```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```
