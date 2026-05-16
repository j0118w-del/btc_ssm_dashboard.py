#!/usr/bin/env python3
"""
Quick start guide for BTC SSM Dashboard
Run this to verify everything is set up correctly
"""

import sys
import os

def check_python():
    """Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required, you have {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_dependencies():
    """Check required packages"""
    required = ['streamlit', 'torch', 'pandas', 'numpy', 'sklearn', 'ccxt']
    missing = []
    
    for pkg in required:
        try:
            __import__(pkg)
            print(f"✅ {pkg}")
        except ImportError:
            print(f"❌ {pkg} missing")
            missing.append(pkg)
    
    if missing:
        print(f"\n💡 Install missing packages:")
        print(f"   pip install {' '.join(missing)}")
        return False
    return True

def check_model():
    """Check for model file"""
    if os.path.exists("btc_ssm.pt"):
        size_mb = os.path.getsize("btc_ssm.pt") / (1024**2)
        print(f"✅ Model found ({size_mb:.1f} MB)")
        return True
    else:
        print("⚠️  btc_ssm.pt not found (optional - will use random weights)")
        print("   To train the model, see training docs")
        return True

def check_gpu():
    """Check GPU availability"""
    try:
        import torch
        if torch.cuda.is_available():
            print(f"✅ GPU: {torch.cuda.get_device_name(0)}")
            print(f"   VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
        else:
            print("⚠️  GPU not available (will use CPU - slower)")
        return True
    except Exception as e:
        print(f"❌ GPU check failed: {e}")
        return False

def check_api():
    """Check API connectivity"""
    try:
        import ccxt
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker('BTC/USDT')
        price = ticker['last']
        print(f"✅ API connected (BTC/USDT: ${price:,.2f})")
        return True
    except Exception as e:
        print(f"❌ API check failed: {e}")
        return False

def run_checks():
    """Run all checks"""
    print("🔍 BTC SSM Dashboard - Environment Check\n")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python),
        ("Dependencies", check_dependencies),
        ("Model File", check_model),
        ("GPU Support", check_gpu),
        ("API Connectivity", check_api),
    ]
    
    results = []
    for name, check_func in checks:
        print(f"\n{name}:")
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Error: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 50)
    print("\n📊 Summary:")
    passed = sum(1 for _, r in results if r)
    total = len(results)
    print(f"   {passed}/{total} checks passed")
    
    if passed == total:
        print("\n✅ All checks passed! Ready to run:")
        print("   streamlit run btc_ssm_dashboard_v2.py")
    else:
        print("\n⚠️  Some checks failed. Please fix before running.")
    
    return passed == total

if __name__ == "__main__":
    success = run_checks()
    sys.exit(0 if success else 1)
