import requests
api_key ="8994f1a1c11840c0984ee56e040227db"
r =("https://newsapi.org/v2/everything?q=tesla&"
    "from=2025-09-19&sortBy=publishedAt&apiKey"
    "=8994f1a1c11840c0984ee56e040227db")
request = requests.get(r)
content = request.json()
print(content["articles"])
for article in content["articles"]:
     print(article["title"])


