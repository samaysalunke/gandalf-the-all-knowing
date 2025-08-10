#!/bin/bash

# MCP Taste Recommendation Server - Deployment Script
# For Pooch AI Hackathon

set -e

echo "🚀 MCP Taste Recommendation Server Deployment"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Python is installed
echo -e "${BLUE}🔍 Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✅ $PYTHON_VERSION found${NC}"
else
    echo -e "${RED}❌ Python 3 not found. Please install Python 3.8+${NC}"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo -e "${BLUE}📦 Creating virtual environment...${NC}"
    python3 -m venv .venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${GREEN}✅ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${BLUE}🔄 Activating virtual environment...${NC}"
source .venv/bin/activate

# Install dependencies
echo -e "${BLUE}📚 Installing dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}✅ Dependencies installed${NC}"

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠️  No .env file found${NC}"
    echo -e "${BLUE}📝 Creating .env from template...${NC}"
    
    if [ -f "env_example.txt" ]; then
        cp env_example.txt .env
        echo -e "${GREEN}✅ .env file created from template${NC}"
        echo -e "${YELLOW}⚠️  Please edit .env file with your credentials:${NC}"
        echo "   - AUTH_TOKEN: Your secret token for MCP authentication"
        echo "   - MY_NUMBER: Your phone number in format {country_code}{number}"
        echo "   - PORT: Server port (default: 8086)"
    else
        echo -e "${RED}❌ env_example.txt not found${NC}"
        exit 1
    fi
else
    echo -e "${GREEN}✅ .env file already exists${NC}"
fi

# Validate code structure
echo -e "${BLUE}🔍 Validating code structure...${NC}"
python3 validate_code.py
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Code validation passed${NC}"
else
    echo -e "${RED}❌ Code validation failed${NC}"
    exit 1
fi

# Check if ngrok is installed
echo -e "${BLUE}🌐 Checking ngrok installation...${NC}"
if command -v ngrok &> /dev/null; then
    echo -e "${GREEN}✅ ngrok found${NC}"
else
    echo -e "${YELLOW}⚠️  ngrok not found${NC}"
    echo "   Please install ngrok from https://ngrok.com/"
    echo "   This is required to expose your server over HTTPS for Pooch AI"
fi

echo ""
echo -e "${GREEN}🎉 Deployment preparation complete!${NC}"
echo ""
echo -e "${BLUE}📋 Next steps:${NC}"
echo "1. Edit .env file with your credentials:"
echo "   nano .env"
echo ""
echo "2. Start the MCP server:"
echo "   source .venv/bin/activate"
echo "   python mcp_starter.py"
echo ""
echo "3. In a new terminal, expose via ngrok:"
echo "   ngrok http 8086"
echo ""
echo "4. Copy the HTTPS URL from ngrok output"
echo ""
echo "5. Connect to Pooch AI:"
echo "   /mcp connect https://your-ngrok-url.ngrok-free.app/mcp your_secret_token"
echo ""
echo -e "${YELLOW}🏆 Built for Pooch AI Hackathon - #BuildWithPouch${NC}"
echo ""

deactivate
