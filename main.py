import requests as requests
from pprint import pprint

class NewsFeed:
    """Representing multiple news titles adn link as a single string"""
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "a8715c41714640fda4107c82e621bba4"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):

        url = f"{self.base_url}" \
              f"q={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body


news_feed = NewsFeed(interest='bitcoin', from_date='2024-04-20', to_date='2024-05-20', language='en')
print(news_feed.get())