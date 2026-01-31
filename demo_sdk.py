#!/usr/bin/env python3
"""Demonstration script showing lmstudio SDK functionality."""

import sys
import os

# Add the src directory to the Python path so we can import lmstudio directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    import lmstudio
    print(f"lmstudio SDK version: {lmstudio.__version__}")
    
    # Test basic imports
    from lmstudio import Client, LLM, Chat
    print("Successfully imported main classes")
    
    # Test creating a client
    client = lmstudio.Client()
    print("Created Client instance")
    
    # Test the convenience API (this will fail without LM Studio running, which is expected)
    try:
        # This uses the default global client
        model = lmstudio.llm()
        print("Created model handle using convenience API")
    except Exception as e:
        print(f"Convenience API failed (expected without LM Studio): {e}")
    
    # Test creating a client with context manager (this will also fail without LM Studio)
    try:
        with lmstudio.Client() as client:
            print("Created client context manager")
            # This would work if LM Studio was running:
            # model = client.llm.model()
            # result = model.respond("Hello, world!")
    except Exception as e:
        print(f"Client context manager failed (expected without LM Studio): {e}")
    
    # Test Chat functionality
    chat = lmstudio.Chat("You are a helpful assistant")
    chat.add_user_message("Hello, how are you?")
    print("Created and used Chat object")
    
    # Test that we can access the sync and async APIs
    from lmstudio import sync_api, async_api
    print("Can access sync and async APIs")
    
    print("\nlmstudio SDK is properly installed and functional!")
    print("To use the SDK with LM Studio:")
    print("   1. Start LM Studio application")
    print("   2. Load a model in LM Studio")
    print("   3. Use the SDK to interact with the model")
    
except ImportError as e:
    print(f"Failed to import lmstudio: {e}")
    print("The SDK may not be properly installed.")
except Exception as e:
    print(f"Unexpected error: {e}")
