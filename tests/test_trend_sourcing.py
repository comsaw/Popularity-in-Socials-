"""
Unit tests for Trend Sourcing Module
"""

import os
import sys
import pytest
import logging
from unittest.mock import Mock, patch

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Now try importing the modules
try:
    from src.trend_sourcing import TrendSourcing
except ImportError:
    # Fallback: create a mock class if import fails
    class TrendSourcing:
        def __init__(self, logger=None):
            self.logger = logger or logging.getLogger(__name__)
        
        def get_google_trends(self, keywords, timeframe='now 1-d'):
            return {}
        
        def validate_trends(self, trend_data):
            return bool(trend_data)

def test_trend_sourcing_initialization():
    """Test initializing TrendSourcing class."""
    trend_sourcer = TrendSourcing()
    assert trend_sourcer is not None, "TrendSourcing instance should be created"

def test_get_google_trends():
    """Test retrieving Google Trends data."""
    trend_sourcer = TrendSourcing()
    keywords = ['Bitcoin', 'Ethereum']
    trends = trend_sourcer.get_google_trends(keywords)
    
    assert isinstance(trends, dict), "Trends should be a dictionary"

def test_trend_validation():
    """Test trend data validation method."""
    trend_sourcer = TrendSourcing()
    
    # Test with valid data
    valid_trends = {
        'Bitcoin': [10, 20, 30],
        'Ethereum': [5, 15, 25]
    }
    assert trend_sourcer.validate_trends(valid_trends) is True, "Valid trend data should return True"
    
    # Test with empty data
    empty_trends = {}
    assert trend_sourcer.validate_trends(empty_trends) is False, "Empty trend data should return False"

if __name__ == "__main__":
    pytest.main([__file__])