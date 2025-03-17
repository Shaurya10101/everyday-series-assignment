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
REDDIT_API_USER_POSTS_BASE = "https://reddit-scraper2.p.rapidapi.com/user_posts_v3"
REDDIT_API_USER_COMMENTS_BASE = "https://reddit-scraper2.p.rapidapi.com/user_comments_v3"
REDDIT_API_SEARCH_POSTS_BASE = "https://reddit-scraper2.p.rapidapi.com/search_posts_v3"
REDDIT_API_SEARCH_COMMENTS_BASE = "https://reddit-scraper2.p.rapidapi.com/search_comments_v3"
REDDIT_API_POSTS_SUBREDDIT_BASE = "https://reddit-scraper2.p.rapidapi.com/sub_posts_v3"
REDDIT_API_POST_COMMENTS_BASE = "https://reddit-scraper2.p.rapidapi.com/post_comments_v3"




mcp = FastMCP("reddit-wrap")

@mcp.tool()
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
                REDDIT_API_USER_COMMENTS_BASE,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return json.dumps(response.json(), indent=2)
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}


@mcp.tool()
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
                REDDIT_API_USER_POSTS_BASE,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return json.dumps(response.json(), indent=2)
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}


@mcp.tool()
async def search_posts(query:str) -> dict[str, Any]:
    """Search For Reddit Posts"""
    params = {
        "query": query,
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
                REDDIT_API_SEARCH_POSTS_BASE,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return json.dumps(response.json(), indent=2)
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}

@mcp.tool()
async def search_comments(query:str) -> dict[str, Any]:
    """Search For Reddit Comments"""
    params = {
        "query": query,
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
                REDDIT_API_SEARCH_COMMENTS_BASE,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return json.dumps(response.json(), indent=2)
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}

@mcp.tool()
async def get_posts_subreddit(subreddit: str) -> dict[str, Any]:
    """Fetch Posts from a Subreddit"""
    params = {
        "subreddit": subreddit,
    }
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                REDDIT_API_POSTS_SUBREDDIT_BASE,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return json.dumps(response.json(), indent=2)
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
            
@mcp.tool()
async def get_comments_post(post_link: str) -> dict[str, Any]:
    """Fetch Comments from a Post"""
    params = {
        "post": post_link,
    }
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                REDDIT_API_POST_COMMENTS_BASE,
                headers=headers,
                params=params
            )
            response.raise_for_status()
            return json.dumps(response.json(), indent=2)
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}


if __name__ == "__main__":
    mcp.run()


