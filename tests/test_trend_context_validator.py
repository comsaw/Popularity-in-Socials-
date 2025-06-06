import pytest
from src.trend_context_validator import TrendContextValidator

def test_valid_trend_context():
    valid_context = {
        'topic': 'Bitcoin Price Surge',
        'source': 'CoinDesk',
        'relevance_score': 85.5,
        'market_sentiment': 'bullish'
    }
    
    result = TrendContextValidator.validate_trend_context(valid_context)
    
    assert result.is_valid is True
    assert result.errors == []
    assert result.sanitized_data is not None

def test_invalid_trend_context_missing_fields():
    invalid_context = {
        'topic': 'Bitcoin'
    }
    
    result = TrendContextValidator.validate_trend_context(invalid_context)
    
    assert result.is_valid is False
    assert len(result.errors) > 0
    assert result.sanitized_data is None

def test_topic_validation():
    test_cases = [
        ('Valid Topic', True),
        ('', False),
        ('A', False),
        ('A' * 200, False),
        ('<script>Malicious Topic</script>', True)
    ]
    
    for topic, expected_validity in test_cases:
        result = TrendContextValidator._validate_topic(topic)
        assert result.is_valid == expected_validity

def test_source_validation():
    test_cases = [
        ('CoinDesk', True),
        ('', False),
        ('A', False),
        ('A' * 100, False)
    ]
    
    for source, expected_validity in test_cases:
        result = TrendContextValidator._validate_source(source)
        assert result.is_valid == expected_validity

def test_relevance_score_validation():
    test_cases = [
        (85.5, True),
        (0, True),
        (100, True),
        (-1, False),
        (101, False),
        ('invalid', False)
    ]
    
    for score, expected_validity in test_cases:
        result = TrendContextValidator._validate_relevance_score(score)
        assert result.is_valid == expected_validity

def test_market_sentiment_validation():
    test_cases = [
        ('bullish', True),
        ('bearish', True),
        ('neutral', True),
        ('Unknown', False),
        (123, False)
    ]
    
    for sentiment, expected_validity in test_cases:
        result = TrendContextValidator._validate_market_sentiment(sentiment)
        assert result.is_valid == expected_validity