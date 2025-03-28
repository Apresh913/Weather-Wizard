import logging
import os
import sys

def setup_logger(name='weather_app'):
    """
    Set up and configure the logger.
    
    Args:
        name (str): Logger name (default: 'weather_app')
        
    Returns:
        logging.Logger: Configured logger
    """
    # Get the logger or create it if it doesn't exist
    logger = logging.getLogger(name)
    
    # If the logger is already configured, return it
    if logger.handlers:
        return logger
    
    # Configure the logger
    logger.setLevel(logging.INFO)
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Add formatter to handler
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    return logger
