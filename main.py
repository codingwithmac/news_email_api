import requests
from send_email import send_email

api_key = "d770e1297db846bc9d8dabb0f06b66b1"
url = ("https://newsapi.org/v2/everything?q=tesla&" \
       "from=2026-09-21&sortBy=publishedAt&apiKey=d770e1297db846bc9d8dabb0f06b66b1")

# Make request to API website
requests = requests.get(url)

# Get dictionary with data
content = requests.json()

# Access the article titles and description

body = "" #this is a string due to send_message input being a string
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

#print(body)
body = body.encode("utf-8")
send_email(message=body)