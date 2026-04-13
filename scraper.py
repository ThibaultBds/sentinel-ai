import feedparser
import requests

# TON WEBHOOK (CORRECT)
WEBHOOK_URL = "https://discord.com/api/webhooks/1493322194086920344/CGzRW3mhMULKuhN_dZQ5JsAkCeshHE_tn6GLCf95Mqb8AXspeZuLoveGHoaG4ZwYG1NH"

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