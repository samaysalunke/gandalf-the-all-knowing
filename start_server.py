#!/usr/bin/env python3
"""
Production Server Starter
Simplified production deployment with health checks and monitoring
"""

import os
import sys
import subprocess
import time
import signal
from pathlib import Path

def check_environment():
    """Check if environment is properly set up"""
    print("🔍 Checking environment...")
    
    # Check if .env exists
    if not Path(".env").exists():
        print("❌ .env file not found. Please create one from env_example.txt")
        return False
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("❌ Virtual environment not activated. Run: source .venv/bin/activate")
        return False
    
    # Check if dependencies are installed
    try:
        import fastapi
        import uvicorn
        import pydantic
        from taste_engine import MasterTasteInterpreter
        print("✅ All dependencies available")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return False

def run_quick_test():
    """Run a quick functionality test"""
    print("🧪 Running quick functionality test...")
    try:
        from mcp_starter import execute_validate, execute_get_taste_recommendations
        
        # Test validate
        result = execute_validate()
        if result.get("status") != "validated":
            print("❌ Validate test failed")
            return False
        
        # Test recommendation
        result = execute_get_taste_recommendations("Something like The Office")
        if not result.get("success"):
            print("❌ Recommendation test failed")
            return False
        
        print("✅ Quick tests passed")
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def start_server():
    """Start the MCP server with production settings"""
    print("🚀 Starting MCP Taste Recommendation Server...")
    
    # Get configuration from environment
    port = os.getenv("PORT", "8086")
    auth_token = os.getenv("AUTH_TOKEN", "")
    my_number = os.getenv("MY_NUMBER", "")
    
    if not auth_token or auth_token == "your_secret_token_here":
        print("⚠️  WARNING: Using default auth token. Please set AUTH_TOKEN in .env")
    
    if not my_number or my_number == "919876543210":
        print("⚠️  WARNING: Using default phone number. Please set MY_NUMBER in .env")
    
    print(f"📱 Phone number: {my_number}")
    print(f"🔐 Auth token: {auth_token[:8]}...")
    print(f"🌐 Port: {port}")
    print(f"📡 Server will be available at: http://localhost:{port}")
    print()
    print("🎯 Ready for ngrok exposure and Pooch AI integration!")
    print("   Next step: ngrok http " + port)
    print()
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        # Start the server
        os.system(f"python mcp_starter.py")
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Server error: {e}")

def main():
    """Main production starter"""
    print("🎬 MCP Taste Recommendation Server - Production Starter")
    print("=" * 60)
    
    # Environment check
    if not check_environment():
        print("\n❌ Environment check failed. Please fix the issues above.")
        return 1
    
    # Quick functionality test
    if not run_quick_test():
        print("\n❌ Functionality test failed. Please check the implementation.")
        return 1
    
    print("✅ All checks passed. Starting production server...\n")
    
    # Start server
    start_server()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
