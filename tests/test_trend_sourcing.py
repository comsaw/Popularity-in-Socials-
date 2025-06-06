"""
Unit tests for Trend Sourcing Module
"""

import pytest
import logging
from src.trend_sourcing import TrendSource, TrendSourcingError

def test_trend_source_initialization():
    """Test trend source initialization with and without logger."""
    custom_logger = logging.getLogger('test_logger')
    trend_source_with_logger = TrendSource(logger=custom_logger)
    trend_source_without_logger = TrendSource()
    
    assert trend_source_with_logger.logger == custom_logger
    assert isinstance(trend_source_without_logger.logger, logging.Logger)

def test_validate_trend_data_success():
    """Test successful trend data validation."""
    trend_source = TrendSource()
    valid_data = [
        {'name': 'Bitcoin', 'score': 95, 'volume': 1000000},
        {'name': 'Ethereum', 'score': 85, 'volume': 500000}
    ]
    
    assert trend_source.validate_trend_data(valid_data) is True

def test_validate_trend_data_failure():
    """Test trend data validation failure scenarios."""
    trend_source = TrendSource()
    
    # Empty data
    assert trend_source.validate_trend_data([]) is False
    
    # Incomplete trend data
    invalid_data = [
        {'name': 'Bitcoin'},
        {'score': 95}
    ]
    
    assert trend_source.validate_trend_data(invalid_data) is False

def test_fetch_trends_not_implemented():
    """Test that fetch_trends raises NotImplementedError."""
    trend_source = TrendSource()
    
    with pytest.raises(NotImplementedError):
        trend_source.fetch_trends()