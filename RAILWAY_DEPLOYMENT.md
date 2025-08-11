# 🚀 Railway.com Deployment Guide

## Quick Deploy Steps

### 1. Sign Up for Railway
- Go to [railway.app](https://railway.app)
- Sign up with your GitHub account
- Verify your email

### 2. Create New Project
- Click "New Project"
- Select "Deploy from GitHub repo"
- Choose your repository: `samaysalunke/gandalf-the-all-knowing`

### 3. Configure Environment Variables
In Railway dashboard → Variables tab, add:
```
AUTH_TOKEN=gandalf_2025
MY_NUMBER=918291077927
DEBUG=false
MCP_PROTOCOL_VERSION=2025-06-18
```

### 4. Deploy
- Railway will auto-detect Python project
- Install dependencies from requirements.txt
- Start server using Procfile
- Provide public HTTPS URL

### 5. Get Your URL
After deployment, you'll get:
`https://your-app-name.railway.app`

### 6. Connect to Puch AI
```
/mcp connect https://your-app-name.railway.app/mcp gandalf_2025
```

## Files Created
- ✅ Procfile: `web: uvicorn mcp_starter:app --host 0.0.0.0 --port $PORT`
- ✅ railway.json: Deployment configuration
- ✅ runtime.txt: Python 3.11 specification
- ✅ requirements.txt: Dependencies (already exists)

## Advantages over ngrok
- ✅ Permanent HTTPS URL
- ✅ Auto-scaling
- ✅ Continuous deployment
- ✅ Professional hosting
- ✅ No tunnel expiration
