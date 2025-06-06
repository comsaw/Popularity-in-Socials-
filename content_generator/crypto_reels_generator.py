from typing import Dict, List
from content_generator.trend_context import TrendContextAnalyzer

def generate_crypto_reel(custom_trend: Dict = None) -> Dict[str, str]:
    """
    Generate a cryptocurrency-focused reel with intelligent trend context.
    
    Args:
        custom_trend: Optional custom trend for forced context injection
    
    Returns:
        Dictionary containing reel components
    """
    # Base script generation logic (simplified for demonstration)
    base_script = """
In the dynamic world of cryptocurrency, understanding market trends is crucial.
Every investment decision requires careful research and strategic thinking.
Stay informed, stay ahead!
"""
    
    # Get trending topics
    trending_topics = TrendContextAnalyzer.get_trending_topics()
    
    # Select trend (use custom trend if provided)
    selected_trend = custom_trend or TrendContextAnalyzer.select_top_trend(trending_topics)
    
    # Inject trend context
    enriched_script = TrendContextAnalyzer.inject_trend_context(base_script, selected_trend)
    
    return {
        "title": f"Crypto Insights: {selected_trend['name']}",
        "script": enriched_script,
        "hashtags": [
            "#Cryptocurrency", 
            "#CryptoTrends", 
            f"#{selected_trend['name'].replace(' ', '')}"
        ],
        "cta": "Learn more about crypto trends!"
    }