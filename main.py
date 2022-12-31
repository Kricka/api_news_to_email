import requests
from send_email import send_email


url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d0726f52e2734be3afb0e922347416ee"
api_key="d0726f52e2734be3afb0e922347416ee"


request=requests.get(url)
data=request.json()


with open('body.txt','w') as file:
    for article in data['articles']:
        file.writelines(article['title']+'\n')
        file.writelines(article['url']+'\n'+'\n')
file.close()


with open('body.txt','r') as file:
    message=file.read()

send_email(message)


