"""
Trend Sourcing Module for Cryptocurrency Content Generation

Provides multiple strategies for sourcing cryptocurrency trends.
"""

import abc
import logging
import typing
import requests
from .credentials import CredentialsManager

class TrendSourcingError(Exception):
    """Base exception for trend sourcing errors."""
    pass

class BaseTrendSource(abc.ABC):
    """
    Abstract base class for cryptocurrency trend sources.
    
    Defines the interface for trend sourcing strategies.
    """
    
    def __init__(self, 
                 credentials_manager: CredentialsManager,
                 logger: typing.Optional[logging.Logger] = None):
        """
        Initialize base trend source.
        
        Args:
            credentials_manager (CredentialsManager): Manages API credentials
            logger (Optional[logging.Logger]): Custom logger
        """
        self.credentials = credentials_manager
        self.logger = logger or logging.getLogger(__name__)
    
    @abc.abstractmethod
    def fetch_trends(self) -> typing.List[dict]:
        """
        Fetch cryptocurrency trends.
        
        Returns:
            List[dict]: Trending cryptocurrency data
        
        Raises:
            TrendSourcingError: If trend fetching fails
        """
        pass
    
    def validate_trend_data(self, data: typing.List[dict]) -> bool:
        """
        Validate retrieved trend data.
        
        Args:
            data (List[dict]): Trend data to validate
        
        Returns:
            bool: Whether the trend data is valid
        """
        if not data:
            self.logger.warning("No trend data retrieved.")
            return False
        
        required_keys = ['name', 'symbol', 'price', 'volume', 'trend_score']
        for trend in data:
            if not all(key in trend for key in required_keys):
                self.logger.error(f"Invalid trend data: {trend}")
                return False
        
        return True

class CoinMarketCapTrendSource(BaseTrendSource):
    """
    Trend sourcing strategy using CoinMarketCap API.
    """
    
    def fetch_trends(self) -> typing.List[dict]:
        """
        Fetch top cryptocurrency trends from CoinMarketCap.
        
        Returns:
            List[dict]: Top trending cryptocurrencies
        
        Raises:
            TrendSourcingError: If API request fails
        """
        try:
            # Retrieve CoinMarketCap API credentials
            credentials = self.credentials.get_credentials('coinmarketcap')
            
            # CoinMarketCap API endpoint for top cryptocurrencies
            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
            
            headers = {
                'X-CMC_PRO_API_KEY': credentials['api_key'],
                'Accept': 'application/json'
            }
            
            # Parameters to fetch top 100 cryptocurrencies by market cap
            params = {
                'start': '1',
                'limit': '100',
                'convert': 'USD'
            }
            
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            
            data = response.json().get('data', [])
            
            # Transform CoinMarketCap data to our trend format
            trends = [
                {
                    'name': crypto['name'],
                    'symbol': crypto['symbol'],
                    'price': crypto['quote']['USD']['price'],
                    'volume': crypto['quote']['USD']['volume_24h'],
                    'trend_score': crypto['cmc_rank']
                } for crypto in data
            ]
            
            # Validate and return trends
            if self.validate_trend_data(trends):
                return trends
            
            raise TrendSourcingError("Invalid trend data from CoinMarketCap")
        
        except Exception as e:
            self.logger.error(f"CoinMarketCap trend sourcing failed: {e}")
            raise TrendSourcingError(f"Trend sourcing error: {e}")

class TrendSourceFactory:
    """
    Factory for creating trend source instances.
    """
    
    @staticmethod
    def create_trend_source(
        source_type: str, 
        credentials_manager: CredentialsManager
    ) -> BaseTrendSource:
        """
        Create a trend source based on the specified type.
        
        Args:
            source_type (str): Type of trend source
            credentials_manager (CredentialsManager): Credentials manager
        
        Returns:
            BaseTrendSource: Instantiated trend source
        
        Raises:
            ValueError: If an unsupported source type is provided
        """
        sources = {
            'coinmarketcap': CoinMarketCapTrendSource
        }
        
        if source_type.lower() not in sources:
            raise ValueError(f"Unsupported trend source: {source_type}")
        
        return sources[source_type.lower()](credentials_manager)