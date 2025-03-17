# Reddit Summary MCP Server

A specialized MCP (Machine Control Protocol) server that analyzes Reddit user data to generate insightful summaries from posts and comments.

## Features

- Fetch user data from Reddit
- Generate summaries of user posts and comments
- Analyze user activity patterns
- Support for multiple data processing endpoints

## Prerequisites

- Python 3.8 or higher
- UV package manager (recommended) or pip
- Reddit API credentials

## Setup

1. Install UV (recommended)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository
```bash
git clone <repository-url>
cd everyday-series-assignment
```

3. Create and activate virtual environment
```bash
uv init
source .venv/bin/activate  # On Unix/macOS
# OR
.venv\Scripts\activate  # On Windows
```

4. Install dependencies
```bash
uv add requirements.txt
```

5. Configure RAPID_API_KEY 
   - Copy `.env.example` to `.env`
   - Update `.env` with your RAPID API credentials

## Usage

1. Copy `mcp_config.json` to the mcp_config.json of the desired client
2. Use the client 



