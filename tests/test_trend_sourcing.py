import unittest
import pandas as pd
from src.trend_sourcing import TrendSourcing

class TestTrendSourcing(unittest.TestCase):
    def setUp(self):
        self.trend_sourcer = TrendSourcing()
    
    def test_get_google_trends(self):
        keywords = ['Bitcoin', 'Ethereum']
        trends = self.trend_sourcer.get_google_trends(keywords)
        
        self.assertIsInstance(trends, pd.DataFrame, "Google Trends should return a DataFrame")
        self.assertTrue(not trends.empty, "Google Trends DataFrame should not be empty")
    
    def test_get_crypto_trends(self):
        cryptocurrencies = ['BTC', 'ETH']
        trends = self.trend_sourcer.get_crypto_trends(cryptocurrencies)
        
        self.assertIsInstance(trends, dict, "Crypto trends should return a dictionary")
        for coin, data in trends.items():
            self.assertIn(coin, cryptocurrencies, f"{coin} not in original request")
    
    def test_get_crypto_news_trends(self):
        keywords = ['cryptocurrency', 'blockchain']
        
        # Will be an empty list if no NewsAPI key
        news_trends = self.trend_sourcer.get_crypto_news_trends(keywords)
        
        self.assertIsInstance(news_trends, list, "News trends should be a list")

if __name__ == '__main__':
    unittest.main()