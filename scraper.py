import feedparser
from datetime import datetime

# RSS CERT-FR
url = "https://www.cert.ssi.gouv.fr/feed/"
feed = feedparser.parse(url)

print("=== SENTINEL AI ===")
print(f"Articles trouvés : {len(feed.entries)}")

for entry in feed.entries[:5]:  # 5 derniers
    title = entry.title
    link = entry.link
    summary = entry.summary[:100] + "..." if len(entry.summary) > 100 else entry.summary
    
    print(f"\nTitre : {title}")
    print(f"Lien : {link}")
    print(f"Résumé : {summary}")
    print("-" * 50)