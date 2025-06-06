# Cryptocurrency Content Generation System

## Trend Sourcing Configuration

### Prerequisites
- Install required dependencies: `pip install -r requirements.txt`

### API Keys
To fully utilize trend sourcing capabilities, configure the following optional API keys:
- NewsAPI Key
- CryptoCompare API Key

### Basic Usage
```python
from src.trend_sourcing import configure_trend_sources

# Optional: Configure with API keys
trend_sourcer = configure_trend_sources(
    newsapi_key='YOUR_NEWSAPI_KEY', 
    cryptocompare_key='YOUR_CRYPTOCOMPARE_KEY'
)

# Get Google Trends
google_trends = trend_sourcer.get_google_trends(['Bitcoin', 'Ethereum'])

# Get Cryptocurrency Market Trends
crypto_trends = trend_sourcer.get_crypto_trends(['BTC', 'ETH'])

# Get Cryptocurrency News Trends
news_trends = trend_sourcer.get_crypto_news_trends(['cryptocurrency', 'blockchain'])
```

### Supported Trend Sources
- Google Trends
- CryptoCompare Market Data
- NewsAPI (optional)

## Development
- Run tests: `pytest tests/`
- Ensure all dependencies are installed