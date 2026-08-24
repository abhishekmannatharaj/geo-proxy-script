import random

import httpx


PROXY_API_URL = (
    "https://proxylister.com/api/v1/proxies"
    "?protocol=http&limit=10"
)


async def get_proxies():

    async with httpx.AsyncClient(timeout=10) as client:

        response = await client.get(PROXY_API_URL)

        response.raise_for_status()

        data = response.json()

    proxies = data.get("results", [])

    if not proxies:
        raise Exception("No proxies available")

    return proxies


async def get_random_proxy():

    proxies = await get_proxies()

    proxy = random.choice(proxies)

    ip = proxy["ip_address"]

    port = proxy["port"]

    country = proxy.get("location", {}).get(
        "country",
        "Unknown"
    )

    city = proxy.get("location", {}).get(
        "city",
        "Unknown"
    )

    proxy_url = f"http://{ip}:{port}"

    return {
        "proxy_url": proxy_url,
        "ip": ip,
        "port": port,
        "country": country,
        "city": city
    }