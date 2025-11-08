import requests
import json
from rich import print_json
from send_email import send_email
api_key = "8994f1a1c11840c0984ee56e040227db"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
"2025-10-08&sortBy=publishedAt&apiKey=8994f1a1c11840c09" \
"84ee56e040227db"
request = requests.get(url)
content = request.json()
print_json(json.dumps(content))
body = ""
for articles in content["articles"]:
    if articles["title"] is not None:
        body =  body + articles["title"] + "\n" + articles["description"] + 2*"\n"
body = body.encode("utf-8")
send_email(message = body)