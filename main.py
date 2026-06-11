import requests

url = "https://www.bi.go.id/id/statistik/informasi-kurs/jisdor/Default.aspx"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("Status Code:", response.status_code)
print(response.text[:3000])
