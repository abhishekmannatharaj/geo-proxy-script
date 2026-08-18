import requests

# Get a proxy from ProxyLister
proxy_api_url = "https://proxylister.com/api/v1/proxies?protocol=http&limit=1"

response = requests.get(proxy_api_url, timeout=10)

print("ProxyLister Status:", response.status_code)

data = response.json()

# Get the first proxy
proxy = data["results"][0]

# Get proxy details automatically
ip = proxy["ip_address"]
port = proxy["port"]
protocol = proxy["protocols"][0]

country = proxy["location"]["country"]
city = proxy["location"]["city"]

print("Proxy IP:", ip)
print("Port:", port)
print("Protocol:", protocol)
print("Country:", country)
print("City:", city)

# Create proxy URL
proxy_url = f"http://{ip}:{port}"

proxies = {
    "http": proxy_url,
    "https": proxy_url
}

# Test URL
url = "http://httpbin.org/ip"

# Make request through proxy
response = requests.get(
    url,
    proxies=proxies,
    timeout=15
)

print("Request Status:", response.status_code)
print("Response:", response.json())