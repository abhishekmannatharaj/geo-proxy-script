from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class ProxyRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "FastAPI Proxy Service Running"}

@app.post("/proxy-request")
def proxy_request(request_data: ProxyRequest):
    try:
        # Step 1: Request a clean, live HTTP proxy list from ProxyScrape API
        proxy_api_url = "https://proxyscrape.com"
        response = requests.get(proxy_api_url, timeout=10)
        
        # Verify if the response is actually valid JSON data
        if response.status_code == 200:
            data = response.json()
            proxies_list = data.get("proxies", [])
            if proxies_list:
                first_proxy = proxies_list[0]
                proxy_url = f"http://{first_proxy['ip']}:{first_proxy['port']}"
            else:
                proxy_url = "http://23.225.30.118:9999" # Fallback if list is empty
        else:
            proxy_url = "http://23.225.30.118:9999" # Fallback if API fails

        # Step 2: Build the network proxy routing layout
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

        # Step 3: Securely route traffic to the target URL through the proxy
        target_response = requests.get(
            request_data.url,
            proxies=proxies,
            timeout=12
        )

        # Step 4: Safely parse response content type
        content_type = target_response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            response_payload = target_response.json()
        else:
            response_payload = {"text_content": target_response.text}

        return {
            "success": True,
            "proxy_used": proxy_url,
            "status_code": target_response.status_code,
            "response": response_payload
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Proxy routing failed: {str(e)}"
        )
