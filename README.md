# Proxy Request & Location Checker

A Python script that retrieves a live public proxy from the ProxyLister API, uses it to make an HTTP request, and reports the proxy's location and country-level statistics.

## What This Script Does

1. Requests a live HTTP proxy from the ProxyLister API.
2. Extracts the proxy's IP address, port, and protocol.
3. Extracts the proxy's location (country and city).
4. Builds a proxy URL and routes a request through it using `requests`.
5. Sends a test request to httpbin to confirm the proxy works.
6. Fetches the list of countries available in the ProxyLister pool.
7. Fetches proxy statistics for the country of the proxy used.

## Technologies Used

- Python 3
- [Requests](https://docs.python-requests.org/)
- [ProxyLister API](https://proxylister.com/api)
- [httpbin](https://httpbin.org) (used as a test target to confirm the proxy is working)

## Requirements

- Python 3.x
- Internet connection

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd geo-proxy-script
```

Install the required package:

```bash
pip install -r requirements.txt
```

## Usage

Run the main script:

```bash
python proxy_task.py
```

The script automatically retrieves a proxy from ProxyLister and prints its details, for example:

```
ProxyLister Status: 200
Proxy IP: 47.251.87.199
Port: 3129
Protocol: HTTP
Country: United States
City: Minkler
Request Status: 200
Response: {'origin': '47.251.87.199'}

Countries endpoint status: 200
Countries available: [...]

Stats for US: {...}
```

### Manual Proxy Version

The repository also includes `manual_proxy.py`, which lets a proxy IP and port be entered manually instead of fetched automatically — useful for testing a specific proxy.

```bash
python manual_proxy.py
```

Example:

```
Enter proxy IP: 47.251.87.199
Enter proxy port: 3129
```

The manually entered proxy is used with the same request logic as the main script.

## Project Structure

```
geo-proxy-script/
│
├── proxy_task.py       # Main script — fetches proxy, tests it, gets location & country stats
├── manual_proxy.py     # Manual proxy entry demo
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Git ignored files
```

## API Reference

This project uses the public [ProxyLister API](https://proxylister.com/api) (no API key required):

- `GET /proxies` — fetch published proxies with filters
- `GET /countries` — list countries present in the proxy pool
- `GET /countries/{code}/proxy-statistics` — stats for a specific country

## Notes

Public proxies can go offline or stop responding at any time, so a proxy retrieved from the API may not always succeed on a given run. This is expected behavior with free proxy pools, not a bug in the script.

This project was built to demonstrate handling HTTP proxies, parsing structured API responses, and working with a third-party REST API in Python.

## Author

Abhishek