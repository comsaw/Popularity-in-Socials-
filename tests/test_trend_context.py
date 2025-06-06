import pytest
from content_generator.trend_context import TrendContextAnalyzer
from content_generator.crypto_reels_generator import generate_crypto_reel

def test_get_trending_topics():
    """Test that trending topics are returned correctly."""
    topics = TrendContextAnalyzer.get_trending_topics()
    assert isinstance(topics, list)
    assert len(topics) > 0
    
    for topic in topics:
        assert "name" in topic
        assert "relevance_score" in topic
        assert 0 <= topic["relevance_score"] <= 1

def test_select_top_trend():
    """Test trend selection logic."""
    topics = TrendContextAnalyzer.get_trending_topics()
    top_trend = TrendContextAnalyzer.select_top_trend(topics)
    
    assert isinstance(top_trend, dict)
    assert "name" in top_trend
    assert "keywords" in top_trend
    assert "description" in top_trend

def test_inject_trend_context():
    """Test trend context injection."""
    base_script = "Original cryptocurrency content."
    topics = TrendContextAnalyzer.get_trending_topics()
    top_trend = TrendContextAnalyzer.select_top_trend(topics)
    
    enriched_script = TrendContextAnalyzer.inject_trend_context(base_script, top_trend)
    
    assert isinstance(enriched_script, str)
    assert base_script in enriched_script
    assert top_trend["name"] in enriched_script or top_trend["description"] in enriched_script

def test_generate_crypto_reel():
    """Test crypto reel generation with trend context."""
    reel = generate_crypto_reel()
    
    assert isinstance(reel, dict)
    assert "title" in reel
    assert "script" in reel
    assert "hashtags" in reel
    assert "cta" in reel
    
    assert len(reel["hashtags"]) > 0
    assert len(reel["script"]) > 0