"""
Credential Management for Trend Sourcing APIs
"""

import os
from typing import Dict, Optional
from dotenv import load_dotenv

class CredentialsManager:
    """
    Manage API credentials for different trend sourcing services.
    
    Supports loading credentials from environment variables or .env file.
    """
    
    def __init__(self, env_file: Optional[str] = None):
        """
        Initialize credentials manager.
        
        Args:
            env_file (Optional[str]): Path to custom .env file. 
                                      Defaults to .env in project root.
        """
        # Load environment variables
        if env_file:
            load_dotenv(env_file)
        else:
            load_dotenv()
    
    def get_credentials(self, service: str) -> Dict[str, str]:
        """
        Retrieve credentials for a specific service.
        
        Args:
            service (str): Name of the API service.
        
        Returns:
            Dict[str, str]: Credentials for the specified service.
        
        Raises:
            ValueError: If credentials are not found.
        """
        credentials = {
            'coingecko': {},  # No API key typically required
            'coinmarketcap': {
                'api_key': os.getenv('COINMARKETCAP_API_KEY', ''),
            },
            'binance': {
                'api_key': os.getenv('BINANCE_API_KEY', ''),
                'api_secret': os.getenv('BINANCE_API_SECRET', ''),
            }
        }
        
        if service.lower() not in credentials:
            raise ValueError(f"No credentials configured for service: {service}")
        
        service_creds = credentials[service.lower()]
        
        # Validate credentials
        if not all(service_creds.values()):
            raise ValueError(f"Missing credentials for {service}")
        
        return service_creds
    
    def validate_credentials(self, service: str) -> bool:
        """
        Validate credentials for a specific service.
        
        Args:
            service (str): Name of the API service.
        
        Returns:
            bool: Whether credentials are valid and complete.
        """
        try:
            creds = self.get_credentials(service)
            return all(creds.values())
        except ValueError:
            return False