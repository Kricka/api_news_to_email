import requests
from send_email import send_email


url="https://newsapi.org/v2/top-headlines?sources=techcrunch&" \
    "apiKey=d0726f52e2734be3afb0e922347416ee&" \
    "language=en"
api_key="d0726f52e2734be3afb0e922347416ee"


request=requests.get(url)
data=request.json()

body=""
for article in data['articles']:
    body="Subject: Today's news" +"\n" \
         + body + "\n" + article['title'] + "\n" + article['description']+"\n" \
         + article['url'] +2*"\n"

body=body.encode("UTF-8")
send_email(body)


