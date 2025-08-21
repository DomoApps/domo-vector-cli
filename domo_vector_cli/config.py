"""Configuration management for Domo Vector CLI."""

import os
import logging
from typing import Optional
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)


@dataclass
class DomoConfig:
    """Configuration settings for Domo API access."""
    developer_token: str
    api_url_base: str
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if not self.developer_token:
            raise ValueError("DOMO_DEVELOPER_TOKEN is required but not set")
        if not self.api_url_base:
            raise ValueError("DOMO_API_URL_BASE is required but not set")
        if not self.api_url_base.startswith(('http://', 'https://')):
            raise ValueError("DOMO_API_URL_BASE must start with http:// or https://")


@dataclass
class ProcessingConfig:
    """Configuration settings for document processing."""
    default_chunk_size: int = 1500
    default_chunk_overlap: int = 200
    batch_size: int = 50
    supported_extensions: tuple = ('.md', '.txt', '.html', '.json')
    
    def __post_init__(self):
        """Validate processing configuration."""
        if self.default_chunk_size <= 0:
            raise ValueError("Chunk size must be positive")
        if self.default_chunk_overlap < 0:
            raise ValueError("Chunk overlap cannot be negative")
        if self.default_chunk_overlap >= self.default_chunk_size:
            raise ValueError("Chunk overlap must be less than chunk size")
        if self.batch_size <= 0:
            raise ValueError("Batch size must be positive")


class ConfigManager:
    """Centralized configuration management."""
    
    def __init__(self):
        self._domo_config: Optional[DomoConfig] = None
        self._processing_config: Optional[ProcessingConfig] = None
    
    @property
    def domo(self) -> DomoConfig:
        """Get Domo API configuration."""
        if self._domo_config is None:
            self._domo_config = self._load_domo_config()
        return self._domo_config
    
    @property
    def processing(self) -> ProcessingConfig:
        """Get document processing configuration."""
        if self._processing_config is None:
            self._processing_config = ProcessingConfig()
        return self._processing_config
    
    def _load_domo_config(self) -> DomoConfig:
        """Load Domo configuration from environment variables."""
        developer_token = os.environ.get("DOMO_DEVELOPER_TOKEN", "")
        api_url_base = os.environ.get("DOMO_API_URL_BASE", "")
        
        logger.debug(f"Loading Domo config - API base: {api_url_base}")
        logger.debug(f"Loading Domo config - Token available: {bool(developer_token)}")
        
        return DomoConfig(
            developer_token=developer_token,
            api_url_base=api_url_base
        )
    
    def validate_required_config(self) -> bool:
        """
        Validate that all required configuration is available.
        
        Returns:
            True if all required config is present, False otherwise
        """
        try:
            _ = self.domo  # This will raise if config is invalid
            return True
        except ValueError as e:
            logger.error(f"Configuration validation failed: {e}")
            return False
    
    def get_headers(self) -> dict:
        """Get HTTP headers for Domo API requests."""
        return {
            "x-domo-developer-token": self.domo.developer_token,
            "Content-Type": "application/json"
        }
    
    def reload(self) -> None:
        """Reload configuration from environment."""
        load_dotenv(override=True)
        self._domo_config = None
        self._processing_config = None


# Global configuration instance
config = ConfigManager()