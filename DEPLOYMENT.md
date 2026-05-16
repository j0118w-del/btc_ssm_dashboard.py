# ☁️ Cloud Deployment Guide

Complete step-by-step instructions for 8 cloud platforms. Choose based on your needs.

## 🏆 Recommended: Streamlit Cloud (Free)

**Best for**: Quick deployment, zero maintenance, always free tier available.

### Setup (5 minutes)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: BTC SSM Dashboard v2"
   git remote add origin https://github.com/YOUR_USERNAME/btc_ssm_dashboard.py.git
   git push -u origin main
   ```

2. **Connect to Streamlit Cloud**
   - Go to https://streamlit.io/cloud
   - Click "New App"
   - Select your repository and branch
   - Main file: `btc_ssm_dashboard_v2.py`
   - Click "Deploy"

3. **Add Secrets** (Optional API keys)
   - In Streamlit Cloud dashboard → Settings → Secrets
   - Add any API keys or config (not needed for this demo)

4. **Access Your App**
   - Public URL: `https://[random-name].streamlit.app`
   - Share with anyone!

**Pros:**
- ✅ Free tier (1 app)
- ✅ Auto-deploys from GitHub (git push = live!)
- ✅ HTTPS included
- ✅ Zero infrastructure

**Cons:**
- ❌ App sleeps after 1 hour inactivity
- ❌ Limited resources (1GB RAM)
- ❌ Data doesn't persist (predictions lost on restart)

---

## 🎯 Alternative: Render (Best Value)

**Best for**: Always-on deployment, $0-7/month, data persistence.

### Setup (10 minutes)

1. **Create Render Account**
   - https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Select your GitHub repo
   - Name: `btc-ssm-dashboard`
   - Runtime: `Python 3.11`
   - Build command: `pip install -r requirements.txt`
   - Start command: `streamlit run btc_ssm_dashboard_v2.py --server.port 10000`

3. **Configure**
   - Instance Type: Free (0.1 CPU, 512MB RAM)
   - Advanced: Add environment variables if needed

4. **Deploy**
   - Click "Create Web Service"
   - Wait 3-5 minutes for deployment
   - Your app is live at `https://btc-ssm-dashboard.onrender.com`

**Pros:**
- ✅ Always-on (no sleeping)
- ✅ Free tier with modest specs
- ✅ Auto-redeploy on git push
- ✅ Data persists in `/app`

**Cons:**
- ❌ Limited free tier (0.1 CPU = slow)
- ❌ Spins down after 15 min inactivity (free tier)
- ❌ Paid tiers start at $7/mo for always-on

---

## 🚀 Advanced: Google Cloud Run (Serverless)

**Best for**: Scalable, only pay for requests, powerful free tier.

### Setup (15 minutes)

1. **Install Cloud SDK**
   ```bash
   # macOS
   brew install google-cloud-sdk
   # Or download from: https://cloud.google.com/sdk/docs/install
   ```

2. **Authenticate**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

3. **Create Cloud Run Service**
   ```bash
   gcloud run deploy btc-ssm-dashboard \
     --source . \
     --platform managed \
     --region us-central1 \
     --memory 512Mi \
     --timeout 600s \
     --allow-unauthenticated
   ```

4. **Access Your Service**
   - URL provided after deployment
   - Example: `https://btc-ssm-dashboard-xxxxx.run.app`

**Pros:**
- ✅ Powerful free tier (2M requests/month)
- ✅ Scales automatically
- ✅ Pay per request (usually free)
- ✅ Global CDN

**Cons:**
- ❌ Cold start delay (3-5 sec first request)
- ❌ Stateless (no data persistence)
- ❌ More complex setup

---

## 💼 Enterprise: AWS ECS (Fargate)

**Best for**: Production workloads, compliance, custom networking.

### Setup (30 minutes)

1. **Create ECR Repository**
   ```bash
   aws ecr create-repository --repository-name btc-ssm-dashboard
   ```

2. **Build & Push Image**
   ```bash
   aws ecr get-login-password --region us-east-1 | \
     docker login --username AWS --password-stdin YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com
   
   docker build -t btc-ssm-dashboard .
   
   docker tag btc-ssm-dashboard:latest \
     YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/btc-ssm-dashboard:latest
   
   docker push YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/btc-ssm-dashboard:latest
   ```

3. **Create ECS Task Definition**
   - AWS Console → ECS → Task Definitions → Create new
   - Container image: `YOUR_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/btc-ssm-dashboard:latest`
   - Port: 8501
   - Memory: 512MB
   - CPU: 256

4. **Create ECS Service**
   - Create new service → Fargate
   - Task definition: your created definition
   - Cluster: new or existing
   - Desired count: 1
   - Load balancer: Application Load Balancer (optional)

5. **Access Application**
   - Get service URL from ECS console
   - Configure custom domain (optional)

**Pros:**
- ✅ Production-grade
- ✅ Auto-scaling available
- ✅ VPC networking
- ✅ CloudWatch monitoring

**Cons:**
- ❌ $0.29/hour per task (~$60/month)
- ❌ Requires AWS account
- ❌ Complex setup

---

## 🌥️ Alternative: Azure Container Instances

**Best for**: Microsoft ecosystem, enterprise customers.

### Setup (20 minutes)

1. **Install Azure CLI**
   ```bash
   brew install azure-cli
   az login
   ```

2. **Create Container Registry**
   ```bash
   az acr create --resource-group myResourceGroup \
     --name btcssmdashboard --sku Basic
   ```

3. **Push Docker Image**
   ```bash
   az acr build --registry btcssmdashboard \
     --image btc-ssm-dashboard:latest .
   ```

4. **Deploy Container Instance**
   ```bash
   az container create \
     --resource-group myResourceGroup \
     --name btc-ssm-dashboard \
     --image btcssmdashboard.azurecr.io/btc-ssm-dashboard:latest \
     --cpu 1 --memory 0.5 \
     --ports 8501 \
     --registry-login-server btcssmdashboard.azurecr.io \
     --registry-username [username] \
     --registry-password [password]
   ```

5. **Get Public IP**
   ```bash
   az container show --resource-group myResourceGroup \
     --name btc-ssm-dashboard --query ipAddress.fqdn
   ```

**Pros:**
- ✅ Simple container deployment
- ✅ Pay-per-second billing
- ✅ No VM management

**Cons:**
- ❌ $0.0000463 per second (~$1.46/day)
- ❌ Limited scaling
- ❌ Requires Azure account

---

## 🏠 Budget: DigitalOcean App Platform

**Best for**: Developers, reasonable cost, simple setup.

### Setup (15 minutes)

1. **Create DigitalOcean Account**
   - https://m.do.co/c/[referral]
   - Get $200 free credit

2. **Connect GitHub**
   - DigitalOcean → Apps → Create App
   - Select GitHub repo
   - Choose branch

3. **Configure**
   - Service type: Web Service
   - Source: Dockerfile
   - HTTP routes: `/`
   - Environment: Production

4. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app is live

5. **Custom Domain** (optional)
   - Add your domain
   - Update DNS records
   - SSL auto-configured

**Pros:**
- ✅ Simple, user-friendly
- ✅ $12/mo starter tier (good value)
- ✅ Auto-scaling available
- ✅ Good support

**Cons:**
- ❌ $12/month minimum (no free tier)
- ❌ Limited free resources

---

## 🎬 Local: Docker Compose (Development)

**Best for**: Local testing before cloud deployment.

```bash
docker-compose up -d
# Opens at http://localhost:8501
```

---

## 📊 Comparison Table

| Platform | Cost | Setup | Performance | Persistence |
|----------|------|-------|-------------|-------------|
| **Streamlit Cloud** | Free | 5 min | Medium | No |
| **Render** | Free/$7 | 10 min | Slow/Good | Yes |
| **Google Cloud Run** | ~Free | 15 min | Fast | No |
| **AWS ECS** | $60/mo | 30 min | Excellent | Yes |
| **Azure ACI** | ~$43/mo | 20 min | Good | Yes |
| **DigitalOcean** | $12/mo | 15 min | Good | Yes |
| **Docker Local** | Free | 5 min | Fast | Yes |

---

## 🔒 Security Best Practices

### Environment Variables
```bash
# Never commit secrets!
# Use platform's secret management:

# Streamlit Cloud: Settings → Secrets
# Render: Environment
# AWS: Secrets Manager
# Azure: Key Vault

# Example .env (local only, in .gitignore):
BINANCE_API_KEY=your_key_here
BINANCE_SECRET=your_secret_here
```

### HTTPS
- ✅ All platforms provide HTTPS by default
- ✅ Certificates auto-renewed

### Rate Limiting
- Dashboard already uses CCXT rate limiting
- No additional config needed

---

## 🚀 Deployment Checklist

Before deploying:
- [ ] `python check_environment.py` passes
- [ ] `btc_ssm.pt` exists (or using random weights)
- [ ] GitHub repository is public (for CI/CD)
- [ ] All dependencies in `requirements.txt`
- [ ] `.gitignore` excludes large files
- [ ] `Dockerfile` builds locally: `docker build -t btc-ssm-dashboard .`

---

## 🆘 Troubleshooting Deployments

### "App keeps restarting"
- Check memory: minimum 512MB required
- Check logs for errors
- Verify Binance API accessible from cloud

### "Predictions missing after restart"
- Expected! Predictions stored in `predictions_history.json`
- Stateless cloud platforms lose local files
- Solution: Use cloud storage (S3, Azure Blob, etc.)

### "Very slow after 5 minutes"
- Likely hitting GPU memory limits
- Set `DEVICE = "cpu"` in code
- Allocate more memory (paid tier)

### "Port already in use"
- Streamlit uses 8501 by default
- In cloud: auto-managed (shouldn't happen)
- Local: `streamlit run --server.port 8502 btc_ssm_dashboard_v2.py`

---

## 📝 Next Steps

1. **Choose platform** based on needs (Streamlit Cloud = easiest)
2. **Follow setup** for your chosen platform
3. **Test locally first**: `docker-compose up`
4. **Monitor logs** after deployment
5. **Share URL** with team!

---

**Questions?** See `README.md` for troubleshooting or `FIXES.md` for technical details.
