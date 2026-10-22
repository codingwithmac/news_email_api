import requests
from send_email import send_email

topic1 = "apple"
topic2 = "iphone"

api_key = "d770e1297db846bc9d8dabb0f06b66b1"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic1}&"
       f"q={topic2}&"
       "sortBy=publishedAt&"
       "language=en&"
       "apiKey=d770e1297db846bc9d8dabb0f06b66b1")

# Make request to API website
requests = requests.get(url)

# Get dictionary with data
content = requests.json()

# Access the article titles and description

body = "" #this is a string due to send_message input being a string
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + (body + article["title"] + "\n"
                + str(article["description"])
                + "\n" + article["url"] + 2*"\n")

#print(body)
body = body.encode("utf-8")
send_email(message=body)