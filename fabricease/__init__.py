"""
FabricEase - A Simple Python Library for Microsoft Fabric SQL Database Connections

Author: Abdulrafiu Izuafa
Description: Makes connecting to and working with Fabric SQL Database incredibly easy.
"""

__version__ = "0.1.0"
__author__ = "Abdulrafiu Izuafa"
__email__ = "your.email@example.com"

from .connection import FabricConnection
from .database import FabricDatabase
from .exceptions import FabricConnectionError, FabricAuthenticationError

# Make the main classes easily accessible
__all__ = [
    'FabricConnection',
    'FabricDatabase', 
    'FabricConnectionError',
    'FabricAuthenticationError'
]

# Simple usage example in docstring
"""
Quick Start Example:

    from fabricease import FabricDatabase
    
    # Option 1: Use environment variables (.env file)
    db = FabricDatabase.from_env()
    
    # Option 2: Direct credentials
    db = FabricDatabase(
        server="your-server.database.fabric.microsoft.com",
        database="your-database",
        client_id="your-client-id",
        client_secret="your-client-secret", 
        tenant_id="your-tenant-id"
    )
    
    # Execute queries easily
    results = db.query("SELECT * FROM employees")
    
    # Insert data easily
    db.insert("employees", {
        "name": "John Doe",
        "email": "john@example.com",
        "salary": 50000
    })
"""