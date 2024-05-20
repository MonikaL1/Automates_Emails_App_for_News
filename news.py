import requests
from pprint import pprint

class NewsFeed:
    """Representing multiple news titles and links as a single string"""
    base_url = "https://newsapi.org/v2/everything?"
    api_key = ""

    def __init__(self, interest, from_date, to_date, language='en'):
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

        # Check for a successful response
        if response.status_code != 200:
            return f"Error: Unable to fetch news, status code: {response.status_code}"

        content = response.json()

        # Debug: Print the full JSON response to understand its structure
        pprint(content)

        if 'articles' not in content:
            return "Error: No articles found in the response."

        articles = content['articles']

        # Check if the articles list is empty
        if not articles:
            return "No articles found for the specified date range and interest."

        email_body = ''
        for article in articles:
            email_body += article['title'] + "\n" + article['url'] + "\n\n"

        return email_body


if __name__ == "__main__":
    news_feed = NewsFeed(interest='bitcoin', from_date='2024-04-20', to_date='2024-05-20', language='en')
    print(news_feed.get())
