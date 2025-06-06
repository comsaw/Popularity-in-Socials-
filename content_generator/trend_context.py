from typing import Dict, List, Any
import random

class TrendContextAnalyzer:
    """
    Manages trend context for content generation, providing intelligent 
    trend-based content enhancement.
    """
    
    @staticmethod
    def get_trending_topics() -> List[Dict[str, Any]]:
        """
        Simulate fetching trending cryptocurrency topics.
        
        Returns:
            List of trending topic dictionaries with relevance and details.
        """
        trending_topics = [
            {
                "name": "Bitcoin Halving",
                "relevance_score": 0.9,
                "keywords": ["bitcoin", "halving", "crypto investment"],
                "description": "Upcoming Bitcoin halving event with potential market impact"
            },
            {
                "name": "Ethereum Layer 2",
                "relevance_score": 0.7,
                "keywords": ["ethereum", "layer 2", "scalability"],
                "description": "Latest developments in Ethereum's scaling solutions"
            },
            {
                "name": "DeFi Innovation",
                "relevance_score": 0.6,
                "keywords": ["defi", "blockchain", "finance"],
                "description": "Emerging trends in decentralized finance"
            }
        ]
        return trending_topics
    
    @staticmethod
    def select_top_trend(trends: List[Dict[str, Any]], min_relevance: float = 0.5) -> Dict[str, Any]:
        """
        Select the most relevant trend based on relevance score.
        
        Args:
            trends: List of trending topics
            min_relevance: Minimum relevance threshold
        
        Returns:
            Most relevant trend or a default trend if no trend meets criteria
        """
        relevant_trends = [trend for trend in trends if trend['relevance_score'] >= min_relevance]
        
        if not relevant_trends:
            return {
                "name": "Crypto Market Overview",
                "keywords": ["cryptocurrency", "market", "trends"],
                "description": "General cryptocurrency market insights"
            }
        
        return max(relevant_trends, key=lambda x: x['relevance_score'])
    
    @staticmethod
    def inject_trend_context(base_script: str, trend: Dict[str, Any]) -> str:
        """
        Intelligently inject trend context into the base script.
        
        Args:
            base_script: Original content script
            trend: Selected trend dictionary
        
        Returns:
            Enriched script with trend context
        """
        trend_injection_templates = [
            f"\n\n🔥 Trending Topic: {trend['name']} 🔥\n{trend['description']}",
            f"\n\n💡 Key Insight: {random.choice(trend['keywords'])} is driving significant interest right now.",
            f"\n\n📊 Market Context: {trend['description']}"
        ]
        
        injection_point = random.choice([0, -1])  # Inject at start or end
        injected_script = base_script.split('\n')
        injected_script.insert(injection_point, random.choice(trend_injection_templates))
        
        return '\n'.join(injected_script)