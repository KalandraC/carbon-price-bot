import requests
import os

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["chat_id"]

message = "Bot berhasil berjalan dari GitHub Actions"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(
    url,
    json={
        "chat_id": chat_id,
        "text": message
    }
)

print(response.text)
