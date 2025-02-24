
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# Replace with your Gemini API endpoint and API key
gemini_api_endpoint = "(link unavailable)"
gemini_api_key = "YOUR_API_KEY"

@app.post("/get-addresses")
async def get_addresses(instnm: list):
    addresses = []
    for college in instnm:
        params = {"name": college, "api_key": gemini_api_key}
        response = requests.get(gemini_api_endpoint, params=params)
        address = response.json()["address"]
        addresses.append({"college": college, "address": address})
    return JSONResponse(content=addresses, media_type="application/json")
