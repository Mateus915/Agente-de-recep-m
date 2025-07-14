import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    print(f"📨 Enviando mensagem para Telegram (chat_id={chat_id})")
    print(f"➡️ Payload: {payload}")
    response = requests.post(url, json=payload)
    print(f"📬 Telegram resposta: {response.status_code} - {response.text}")
    return response.ok

