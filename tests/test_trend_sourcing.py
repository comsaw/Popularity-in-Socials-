"""
Unit tests for the TrendSourcing module.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.trend_sourcing import TrendSourcing

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
    assert len(trends) > 0, "Trends data should not be empty"

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