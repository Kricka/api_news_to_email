import requests
from send_email import send_email
from nltk.sentiment import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()


url="http://api.mediastack.com/v1/news?access_key=f6eaa744d81f95ec9e98d9073d4bc39a" \
    "&countries=us,gb"
api_key="f6eaa744d81f95ec9e98d9073d4bc39a"


request=requests.get(url)
data=request.json()

body=""
for article in data['data']:
    polarities=analyzer.polarity_scores(article['description'])
    pos=polarities['pos']
    neg = polarities['neg']
    if pos > neg:
        body="Subject: Today's news" + "\n" \
             + body + "\n" + article['title'] + "\n" + article['description']+"\n" \
             + article['url'] +2*"\n"

body=body.encode("UTF-8")
send_email(body)


