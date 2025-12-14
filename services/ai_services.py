import httpx

AI_BASE_URL = "http://127.0.0.1:9000/ai"

async def summarize_book(text: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AI_BASE_URL}/summarize-book", json={"text": text})
        response.raise_for_status()
        return response.json()


# async def generate_tags(title: str, description: str = ""):
#     payload = {"title": title, "description": description}
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f"{AI_BASE_URL}/generate-tags", json=payload)
#         response.raise_for_status()
#         return response.json()
async def generate_tags(text: str) -> list[str]:
    """
    Generate tags/categories from the text using your AI model (OpenAI or any LLM)
    """
    # Dummy example (replace with real AI call)
    keywords = ["fiction", "adventure", "kids"]  # replace with AI response
    return keywords


async def rewrite_blog(content: str, tone: str = "professional"):
    payload = {"content": content, "tone": tone}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AI_BASE_URL}/rewrite-blog", json=payload)
        response.raise_for_status()
        return response.json()


async def ai_search(query: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AI_BASE_URL}/search", json={"query": query})
        response.raise_for_status()
        return response.json()
