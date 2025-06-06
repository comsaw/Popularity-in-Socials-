import typing
import requests
import pandas as pd
from pytrends.request import TrendReq
from newsapi import NewsApiClient
import cryptocompare

class TrendSourcing:
    """
    A comprehensive trend sourcing class for cryptocurrency content generation.
    
    Aggregates trends from multiple sources including Google Trends, 
    News APIs, and Cryptocurrency market data.
    """
    
    def __init__(self, 
                 newsapi_key: typing.Optional[str] = None, 
                 cryptocompare_key: typing.Optional[str] = None):
        """
        Initialize trend sourcing with optional API keys.
        
        Args:
            newsapi_key (str, optional): API key for NewsAPI
            cryptocompare_key (str, optional): API key for CryptoCompare
        """
        self.pytrends = TrendReq()
        
        # Optional API clients
        self.newsapi = NewsApiClient(api_key=newsapi_key) if newsapi_key else None
        cryptocompare.cryptocompare._api_key = cryptocompare_key
    
    def get_google_trends(self, keywords: typing.List[str], timeframe: str = 'today 1-m') -> pd.DataFrame:
        """
        Fetch Google Trends data for specified keywords.
        
        Args:
            keywords (List[str]): List of keywords to track
            timeframe (str): Timeframe for trend data
        
        Returns:
            pd.DataFrame: Trend data for specified keywords
        """
        try:
            self.pytrends.build_payload(keywords, timeframe=timeframe)
            return self.pytrends.interest_over_time()
        except Exception as e:
            print(f"Google Trends Error: {e}")
            return pd.DataFrame()
    
    def get_crypto_trends(self, cryptocurrencies: typing.List[str]) -> typing.Dict:
        """
        Fetch cryptocurrency market trends.
        
        Args:
            cryptocurrencies (List[str]): List of cryptocurrency symbols
        
        Returns:
            Dict: Price and trend information for specified cryptocurrencies
        """
        try:
            return {
                coin: cryptocompare.get_price(coin, full=True)
                for coin in cryptocurrencies
            }
        except Exception as e:
            print(f"Cryptocurrency Trend Error: {e}")
            return {}
    
    def get_crypto_news_trends(self, keywords: typing.List[str], page_size: int = 10) -> typing.List:
        """
        Fetch news trends related to cryptocurrency keywords.
        
        Args:
            keywords (List[str]): Keywords to search for
            page_size (int): Number of news articles to retrieve
        
        Returns:
            List: Trending news articles
        """
        if not self.newsapi:
            print("NewsAPI key not configured")
            return []
        
        try:
            return [
                article 
                for keyword in keywords 
                for article in self.newsapi.get_everything(
                    q=keyword, 
                    language='en', 
                    page_size=page_size
                )['articles']
            ]
        except Exception as e:
            print(f"News Trend Error: {e}")
            return []

# Optional configuration and testing method
def configure_trend_sources(newsapi_key: str = None, cryptocompare_key: str = None):
    """
    Configure global trend sourcing with API keys.
    
    Args:
        newsapi_key (str, optional): NewsAPI key
        cryptocompare_key (str, optional): CryptoCompare API key
    """
    return TrendSourcing(newsapi_key, cryptocompare_key)