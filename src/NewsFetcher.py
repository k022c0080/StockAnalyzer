from newsapi import NewsApiClient

class NewsFetcher:
    def __init__(self, api_key):
        self.newsapi = NewsApiClient(api_key=api_key)

    def fetch_news(self, query, start_date, end_date):
        try:
            articles = self.newsapi.get_everything(
                q=query,
                from_param=start_date,
                to=end_date,
                language="en",
                sort_by="relevancy",
                page_size=100
            )
            return articles['articles']
        except Exception as e:
            print(f"Error fetching news: {e}")
            return []
