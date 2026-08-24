import httpx

from models import RequestConfig
from proxy_service import get_random_proxy


async def execute_request(config: RequestConfig):

    last_error = None

    for attempt in range(
        1,
        config.max_retries + 1
    ):

        proxy_info = None
        proxy_url = None

        try:

            if config.use_proxy:

                proxy_info = await get_random_proxy()

                proxy_url = proxy_info["proxy_url"]

                client = httpx.AsyncClient(
                    proxy=proxy_url,
                    timeout=config.timeout
                )

            else:

                client = httpx.AsyncClient(
                    timeout=config.timeout
                )

            async with client:

                response = await client.request(
                    method=config.method.upper(),
                    url=str(config.url),
                    headers=config.headers,
                    params=config.params,
                    json=config.body
                )

                try:

                    response_data = response.json()

                except Exception:

                    response_data = response.text

                return {

                    "success": True,

                    "attempt": attempt,

                    "proxy_used": proxy_info,

                    "status_code": response.status_code,

                    "response": response_data

                }

        except Exception as error:

            last_error = str(error)

    return {

        "success": False,

        "error": last_error,

        "attempts": config.max_retries

    }