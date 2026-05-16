#!/bin/bash

# BTC SSM Dashboard Setup Script
set -e

echo "🚀 BTC SSM Dashboard Setup"
echo "============================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "  Python $PYTHON_VERSION"

# Create virtual environment
echo "✓ Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "✓ Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "✓ Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
mkdir -p data logs

echo ""
echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "   1. Activate environment: source venv/bin/activate"
echo "   2. Run dashboard: streamlit run btc_ssm_dashboard_v2.py"
echo ""
echo "🌐 Dashboard will open at: http://localhost:8501"
echo ""
