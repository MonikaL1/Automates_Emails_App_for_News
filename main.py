# Api key: a8715c41714640fda4107c82e621bba4
import requests as requests
from pprint import pprint

class NewsFeed:
    def __init__(self, data):
        self.data = data

    def get(self):
        pass


url = "https://newsapi.org/v2/everything?" \
      "q=bitcoin&" \
      "from=2024-04-20&" \
      "to=2024-05-20&" \
      "sortBy=publishedAt&" \
      "language=en&" \
      "apiKey=a8715c41714640fda4107c82e621bba4"
response = requests.get(url)
content = response.json()
x = content['articles'][2]['url']
print(x)
pprint(content)

