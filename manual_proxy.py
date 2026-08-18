import requests

# You enter the proxy details manually
proxy_ip = input("Enter proxy IP: ")
proxy_port = input("Enter proxy port: ")

proxy_url = f"http://{proxy_ip}:{proxy_port}"

proxies = {
    "http": proxy_url,
    "https": proxy_url
}

url = "http://httpbin.org/ip"

response = requests.get(
    url,
    proxies=proxies,
    timeout=15
)

print("Status Code:", response.status_code)
print("Response:", response.json())
