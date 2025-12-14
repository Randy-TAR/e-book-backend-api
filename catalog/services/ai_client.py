import requests

FASTAPI_URL = "http://127.0.0.1:9000/ai"  # FastAPI base URL

def summarize_book(text: str):
    url = f"{FASTAPI_URL}/summarize-book"
    payload = {"text": text}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

def generate_tags(text: str):
    url = f"{FASTAPI_URL}/generate-tags"
    payload = {"text": text}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
