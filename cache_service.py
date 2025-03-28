import time
from logger import setup_logger

class CacheService:
    """Simple in-memory cache service with time-based expiration."""
    
    def __init__(self, expiry=300):
        """
        Initialize the cache service.
        
        Args:
            expiry (int): Cache expiry time in seconds (default: 300)
        """
        self.cache = {}
        self.expiry = expiry
        self.logger = setup_logger()
        self.logger.info(f"Cache service initialized with {expiry}s expiry time")
    
    def get(self, key):
        """
        Get a value from the cache.
        
        Args:
            key (str): Cache key
            
        Returns:
            Any: Cached value, or None if not found or expired
        """
        if key in self.cache:
            value, timestamp = self.cache[key]
            
            # Check if the cache entry has expired
            if time.time() - timestamp < self.expiry:
                self.logger.debug(f"Cache hit for key: {key}")
                return value
            else:
                # Remove expired entry
                self.logger.debug(f"Cache entry expired for key: {key}")
                del self.cache[key]
        
        self.logger.debug(f"Cache miss for key: {key}")
        return None
    
    def set(self, key, value):
        """
        Set a value in the cache.
        
        Args:
            key (str): Cache key
            value (Any): Value to cache
        """
        self.logger.debug(f"Setting cache for key: {key}")
        self.cache[key] = (value, time.time())
    
    def delete(self, key):
        """
        Delete a value from the cache.
        
        Args:
            key (str): Cache key
            
        Returns:
            bool: True if deleted, False if key not found
        """
        if key in self.cache:
            self.logger.debug(f"Deleting cache for key: {key}")
            del self.cache[key]
            return True
        
        self.logger.debug(f"Attempted to delete non-existent cache key: {key}")
        return False
    
    def clear(self):
        """Clear all cache entries."""
        self.logger.info("Clearing all cache entries")
        self.cache = {}
    
    def cleanup(self):
        """Remove all expired cache entries."""
        keys_to_delete = []
        
        for key, (_, timestamp) in self.cache.items():
            if time.time() - timestamp >= self.expiry:
                keys_to_delete.append(key)
        
        for key in keys_to_delete:
            del self.cache[key]
        
        self.logger.info(f"Cache cleanup: removed {len(keys_to_delete)} expired entries")
