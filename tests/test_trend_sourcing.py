"""
Unit tests for Trend Sourcing Module
"""

import pytest
import logging
from unittest.mock import Mock, patch
from src.trend_sourcing import (
    BaseTrendSource, 
    CoinMarketCapTrendSource, 
    TrendSourceFactory,
    TrendSourcingError
)
from src.trend_sourcing.credentials import CredentialsManager

class MockCredentialsManager:
    """Mock credentials manager for testing."""
    def get_credentials(self, service):
        return {'api_key': 'test_key'} if service == 'coinmarketcap' else {}

def test_base_trend_source_initialization():
    """Test base trend source initialization."""
    cred_manager = MockCredentialsManager()
    
    class ConcreteSource(BaseTrendSource):
        def fetch_trends(self):
            return []
    
    source = ConcreteSource(cred_manager)
    
    assert source.credentials == cred_manager
    assert isinstance(source.logger, logging.Logger)

def test_validate_trend_data():
    """Test trend data validation."""
    cred_manager = MockCredentialsManager()
    
    class ConcreteSource(BaseTrendSource):
        def fetch_trends(self):
            return []
    
    source = ConcreteSource(cred_manager)
    
    # Valid trend data
    valid_data = [
        {
            'name': 'Bitcoin', 
            'symbol': 'BTC', 
            'price': 50000, 
            'volume': 1000000, 
            'trend_score': 1
        }
    ]
    
    assert source.validate_trend_data(valid_data) is True
    
    # Invalid trend data
    invalid_data = [{'name': 'Incomplete'}]
    assert source.validate_trend_data(invalid_data) is False

@patch('requests.get')
def test_coinmarketcap_trend_source(mock_get):
    """Test CoinMarketCap trend source."""
    # Mock successful API response
    mock_response = Mock()
    mock_response.json.return_value = {
        'data': [
            {
                'name': 'Bitcoin',
                'symbol': 'BTC',
                'quote': {
                    'USD': {
                        'price': 50000,
                        'volume_24h': 1000000
                    }
                },
                'cmc_rank': 1
            }
        ]
    }
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response
    
    # Create trend source
    cred_manager = MockCredentialsManager()
    trend_source = CoinMarketCapTrendSource(cred_manager)
    
    # Fetch trends
    trends = trend_source.fetch_trends()
    
    assert len(trends) == 1
    assert trends[0]['name'] == 'Bitcoin'
    assert trends[0]['symbol'] == 'BTC'

def test_trend_source_factory():
    """Test trend source factory."""
    cred_manager = MockCredentialsManager()
    
    # Test creating CoinMarketCap source
    source = TrendSourceFactory.create_trend_source('coinmarketcap', cred_manager)
    assert isinstance(source, CoinMarketCapTrendSource)
    
    # Test invalid source type
    with pytest.raises(ValueError):
        TrendSourceFactory.create_trend_source('invalid_source', cred_manager)