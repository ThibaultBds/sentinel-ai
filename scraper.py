import feedparser
import requests

# TON WEBHOOK (CORRECT)
from dotenv import load_dotenv

load_dotenv()
import os 
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

url = "https://www.cert.ssi.gouv.fr/feed/"
feed = feedparser.parse(url)

print("=== SENTINEL AI v0.2 ===")

for entry in feed.entries[:1]:  # 1 seule alerte
    # ALERTE Discord
    data = {
        "content": f"🚨 **{entry.title}**\n🔗 {entry.link}"
    }
    response = requests.post(WEBHOOK_URL, json=data)
    
    if response.status_code == 204:
        print(f"✅ Alerte envoyée : {entry.title}")
    else:
        print(f"❌ Erreur Discord : {response.status_code}")
    break