import requests
import json
from rich import print_json

api_key = "8994f1a1c11840c0984ee56e040227db"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
"2025-10-05&sortBy=publishedAt&apiKey" \
"=8994f1a1c11840c0984ee56e040227db"
request = requests.get(url)
content = request.json()
print(json.dumps(content, indent=4,sort_keys=True))
print_json(data=content)
print(content["articles"])
for article in content["articles"]:
    print(article['title'])
    print(article['description'])
