import requests
from send_email import send_email


url="https://newsapi.org/v2/everything?q=tesla&" \
    "from=2022-12-01&sortBy=publishedAt&" \
    "language=en&" \
    "apiKey=d0726f52e2734be3afb0e922347416ee"
api_key="d0726f52e2734be3afb0e922347416ee"


request=requests.get(url)
data=request.json()

body=""
for article in data['articles'][:20]:
    body="Subject: Today's news" + "\n" \
         + body + "\n" + article['title'] + "\n" + article['description']+"\n" \
         + article['url'] +2*"\n"

body=body.encode("UTF-8")
send_email(body)


