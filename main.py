import requests
import json
from rich import print_json
from send_email import send_email
topic="tesla"
api_key = "8994f1a1c11840c0984ee56e040227db"
url = f"https://newsapi.org/v2/everything?q={topic}" \
"&from=2025-10-09&sortBy=publishedAt&apiKey=8994f1a1c11840c0984ee56e040227db" \
"&language=en"
request = requests.get(url)
content = request.json()
print_json(json.dumps(content))
body = ""
for articles in content["articles"][:20]:
    if articles["title"] is not None:
        body =  "Subject: Today's News"+ "\n" + body + articles["title"] + "\n" + articles["description"] + "\n" + articles["url"] + 2*"\n"
body = body.encode("utf-8")
send_email(message = body)