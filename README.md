# 📊 BTC Institutional SSM Dashboard v2.0

**Real-time Bitcoin prediction dashboard powered by State Space Model (SSM) neural networks.**

## ✨ Features

- 🎯 **Real-time 4h Predictions** - State Space Model forecasts next candle
- 💰 **Live Price Data** - Binance OHLCV via CCXT API
- 📈 **Advanced Metrics** - Sharpe ratio, max drawdown, win rate
- 🔥 **Market Regimes** - HIGH VOL, TRENDING, COMPRESSION detection
- 🎨 **Beautiful UI** - Dark theme optimized for trading
- ⚡ **Production Ready** - All 5 critical fixes applied
- 🚀 **Cloud Deployable** - Docker, Streamlit Cloud, AWS, GCP

## 🔧 All 5 Critical Fixes Applied

| Fix | Problem | Solution |
|-----|---------|----------|
| **#1** | 60s UI freeze | Non-blocking session state refresh ✅ |
| **#2** | Memory leaks | Clean model lifecycle management ✅ |
| **#3** | API rate limits | 4-minute cache (75% fewer calls) ✅ |
| **#4** | Distribution shift | Persistent scaler saved to disk ✅ |
| **#5** | Fake metrics | Calibrated confidence + real backtesting ✅ |

## 🚀 Quick Start

### Local (30 seconds)

```bash
chmod +x setup.sh
./setup.sh
source venv/bin/activate
streamlit run btc_ssm_dashboard_v2.py
```

Opens at `http://localhost:8501`

### Docker (No setup)

```bash
docker-compose up -d
```

Opens at `http://localhost:8501`

### Streamlit Cloud (5 minutes)

1. Go to https://streamlit.io/cloud
2. Click "New app"
3. Paste: `https://github.com/j0118w-del/btc_ssm_dashboard.py`
4. Select `btc_ssm_dashboard_v2.py`
5. Click "Deploy"

## 📋 Requirements

- Python 3.8+
- PyTorch 2.0+
- Streamlit 1.28+
- CCXT 4.0+
- scikit-learn

See `requirements.txt` for all dependencies.

## 📊 Dashboard Sections

### Metrics
- Current Price
- Forecast Price (next 4h)
- Signal (LONG/SHORT/NEUTRAL)
- Confidence (20-100%)
- Market Regime

### Key Levels
Institutional support/resistance zones:
- Macro Cycle Top: $126,198
- Major Resistance: $82,750
- Immediate Trend Support: $74,800
- Macro Wedge Boundary: $72,800
- Deep Macro Floor: $59,973

### Charts
- 300-candle price history
- 100-prediction forecast history

### Backtesting Metrics
- **Sharpe Ratio**: Risk-adjusted returns
- **Max Drawdown**: Largest loss
- **Win Rate**: Directional accuracy

## 🔐 Configuration

Edit these variables in `btc_ssm_dashboard_v2.py`:

```python
SYMBOL = 'BTC/USDT'          # Trading pair
TIMEFRAME = '4h'             # Candle timeframe
LIMIT = 300                  # Historical candles
MODEL_PATH = "btc_ssm.pt"    # Your trained model
DEVICE = "cuda"              # GPU or CPU
CACHE_TTL = 240              # API cache (seconds)
REFRESH_INTERVAL = 240       # Auto-refresh (seconds)
```

## 🤖 Using Your Model

1. Train your SSM model separately
2. Save as `btc_ssm.pt` in project root
3. Dashboard will auto-load it on startup
4. If no model found, uses random weights (for demo)

## 🌥️ Cloud Deployment

See `DEPLOYMENT.md` for:
- **Streamlit Cloud** (Free)
- **Render** ($7/mo)
- **Google Cloud Run** (~Free)
- **AWS ECS** ($60/mo)
- **Azure ACI** ($43/mo)
- **DigitalOcean** ($12/mo)

## 🛠️ Troubleshooting

### "ModuleNotFoundError: No module named 'ccxt'"
```bash
pip install -r requirements.txt
```

### "CUDA out of memory"
Edit `btc_ssm_dashboard_v2.py` line 25:
```python
DEVICE = "cpu"  # Use CPU instead
```

### "App keeps restarting"
- Check logs: Streamlit Cloud → Manage app → Logs
- Minimum 512MB RAM required
- Verify API connectivity to Binance

### "Predictions missing after restart"
- Expected! `predictions_history.json` is local
- Use cloud storage for persistence (S3, Blob, etc.)

## 📚 Documentation

- `FIXES.md` - Technical deep-dive on all 5 fixes
- `DEPLOYMENT.md` - 8 cloud platforms with step-by-step guides
- `check_environment.py` - Verify setup before running

## 📞 Support

If issues occur:
1. Run: `python check_environment.py`
2. Check logs: `streamlit run btc_ssm_dashboard_v2.py --logger.level=debug`
3. See `DEPLOYMENT.md` troubleshooting section

## 📄 License

MIT

## 🎉 Ready?

```bash
source venv/bin/activate
streamlit run btc_ssm_dashboard_v2.py
```

Your dashboard is live! 🚀
