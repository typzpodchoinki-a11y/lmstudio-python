#!/usr/bin/env python3
"""Simple test script to verify lmstudio SDK installation and basic functionality."""

import sys
import os

# Add the src directory to the Python path so we can import lmstudio directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    # Install missing dependencies first
    import subprocess
    import importlib
    
    required_packages = ['typing_extensions', 'msgspec', 'httpx', 'anyio', 'httpx_ws']
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"Found {package}")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    
    import lmstudio
    print(f"Successfully imported lmstudio SDK version: {lmstudio.__version__}")
    
    # Test basic imports
    from lmstudio import Client, LLM, Chat
    print("Successfully imported main classes: Client, LLM, Chat")
    
    # Test that we can create a client (this will fail if LM Studio is not running)
    try:
        client = lmstudio.Client()
        print("Successfully created Client instance")
        
        # Try to connect (this will fail if LM Studio is not running, which is expected)
        try:
            client.connect()
            print("Successfully connected to LM Studio")
        except Exception as e:
            print(f"Connection failed (expected if LM Studio is not running): {e}")
            
    except Exception as e:
        print(f"Failed to create Client: {e}")
        
except ImportError as e:
    print(f"Failed to import lmstudio: {e}")
    print("The SDK may not be properly installed or accessible.")
