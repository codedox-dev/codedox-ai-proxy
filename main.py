from fastapi import FastAPI, Request
import os
import requests

app = FastAPI()

# Telegram Bot Token and fallback tokens
BOT_TOKENS = os.getenv("BOT_TOKENS", "").split(",")
PAIR_LIMIT = 10

# Simulated database
linked_users = {}

@app.get("/")
def root():
    return {"status": "Anonymous Telegram Bot API Running"}

@app.post("/webhook/{bot_token}")
async def telegram_webhook(bot_token: str, req: Request):
    data = await req.json()
    message = data.get("message") or data.get("edited_message")
    if not message:
        return {"ok": True}

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text.startswith("/start"):
        msg = "Welcome to Anonymous Bot 🤖\n\nUse /pair <phone> to link your WhatsApp"
        send_message(bot_token, chat_id, msg)
    elif text.startswith("/pair"):
        parts = text.strip().split(" ")
        if len(parts) == 2 and parts[1].isdigit():
            phone = parts[1]
            user_data = linked_users.get(chat_id, [])
            if len(user_data) < PAIR_LIMIT:
                user_data.append(phone)
                linked_users[chat_id] = user_data
                send_message(bot_token, chat_id, f"✅ Paired with {phone}")
            else:
                send_message(bot_token, chat_id, "❌ You have reached the limit of 10 pairings.")
        else:
            send_message(bot_token, chat_id, "⚠️ Use format: /pair 234xxxxxxxxxx")
    elif text.startswith("/help"):
        send_message(bot_token, chat_id, "/start - Welcome\n/pair <phone> - Pair WhatsApp\n/help - Show help")
    else:
        send_message(bot_token, chat_id, "🤖 Unknown command.")

    return {"ok": True}

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})
