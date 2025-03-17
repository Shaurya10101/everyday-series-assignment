import json 
import httpx
import os
from dotenv import load_dotenv
from typing import Any
from mcp.server.fastmcp import FastMCP

load_dotenv()



RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
if not RAPIDAPI_KEY:
    raise ValueError("API key not found.")

RAPIDAPI_HOST = "reddit-scraper2.p.rapidapi.com"
REDIT_API_POSTS_BASE = "https://reddit-scraper2.p.rapidapi.com/user_posts_v3"
REDIT_API_COMMENTS_BASE = "https://reddit-scraper2.p.rapidapi.com/user_comments_v3"

mcp = FastMCP("reddit-wrap")

async def get_user_comments(username: str) -> dict[str, Any]:
    """Fetch Reddit Profile Data"""
    params = {
        "user": f"https://www.reddit.com/user/{username}/",
        "sort": "NEW",
        "time": "ALL"
    }
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                REDIT_API_COMMENTS_BASE,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return {"error": f"User '{username}' not found"}
            return {"error": f"HTTP error occurred: {str(e)}"}
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}

async def get_user_posts(username: str) -> dict[str, Any]:
    """Fetch Reddit Profile Data"""
    params = {
        "user": f"https://www.reddit.com/user/{username}/",
        "sort": "NEW",
        "time": "ALL"
    }
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                REDIT_API_POSTS_BASE,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return {"error": f"User '{username}' not found"}
            return {"error": f"HTTP error occurred: {str(e)}"}
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}



@mcp.tool()
async def get_user_data(username:str)-> dict[str, Any]:
    """Fetch Reddit Profile Data"""
    posts = await get_user_posts(username)
    comments = await get_user_comments(username)
    data = {"posts": posts, "comments": comments}
    if not data["posts"] or not data["comments"]:
        return {"error": f"User '{username}' not found"}
    return json.dumps(data, indent=2)

# async def main():
#     # Try with a known active Reddit user
#     username = "AngelaTheDruid"  # Example from the provided code
#     result = await get_user_data(username)
#     print(f"\nResults for user '{username}':\n")
#     print(json.dumps(result, indent=2))

if __name__ == "__main__":
    mcp.run()


