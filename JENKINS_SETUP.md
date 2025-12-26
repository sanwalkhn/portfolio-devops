# Jenkins Automatic Deployment Setup Guide

## Problem: Changes not going live automatically

Follow these steps to enable automatic deployment when you push to GitHub.

## Step 1: Install Required Jenkins Plugins

1. Go to **Jenkins Dashboard** → **Manage Jenkins** → **Plugins**
2. Install these plugins (if not already installed):
   - ✅ **GitHub plugin**
   - ✅ **GitHub Branch Source Plugin**
   - ✅ **Pipeline: GitHub Plugin**

## Step 2: Configure Jenkins Job

1. Open your pipeline: **portfolio-devops-pipeline**
2. Click **Configure**
3. Scroll to **Build Triggers** section
4. ✅ Check **GitHub hook trigger for GITScm polling**
5. ✅ Check **Poll SCM** (as backup) - Schedule: `H/2 * * * *` (every 2 minutes)
6. Click **Save**

## Step 3: Setup GitHub Webhook

### Option A: If Jenkins is accessible from internet

1. Go to your GitHub repository: `https://github.com/sanwalkhn/portfolio-devops`
2. Click **Settings** → **Webhooks** → **Add webhook**
3. **Payload URL:** `http://YOUR_JENKINS_IP:8080/github-webhook/`
   - Example: `http://192.168.1.100:8080/github-webhook/`
4. **Content type:** `application/json`
5. **Secret:** (Leave empty or add if you configured one)
6. **Events:** Select **Just the push event**
7. Click **Add webhook**

### Option B: If Jenkins is on localhost/private network

Use **ngrok** or similar tool to expose Jenkins:

```bash
# Install ngrok
ngrok http 8080

# Use the ngrok URL in GitHub webhook
# Example: https://abc123.ngrok.io/github-webhook/
```

## Step 4: Test the Setup

1. Make a small change in your code
2. Commit and push:
```bash
git add .
git commit -m "Test automatic deployment"
git push origin main
```

3. Check Jenkins:
   - Pipeline should automatically start building
   - Check **Build History** to see new build triggered

## Step 5: Verify Webhook is Working

1. In GitHub: **Settings** → **Webhooks**
2. Click on your webhook
3. Check **Recent Deliveries** - should show successful deliveries (200 status)

## Troubleshooting

### Webhook not triggering?

1. **Check Jenkins URL:**
   - Go to **Manage Jenkins** → **Configure System**
   - Set **Jenkins URL** correctly (e.g., `http://your-ip:8080`)

2. **Check GitHub Plugin:**
   - **Manage Jenkins** → **Configure System**
   - Scroll to **GitHub** section
   - Add GitHub server if needed

3. **Check Jenkins Logs:**
   - **Manage Jenkins** → **System Log**
   - Look for webhook-related errors

### Poll SCM not working?

1. Check **Git Polling Log** in your pipeline
2. Verify repository URL is correct
3. Check Git credentials are configured

### Manual Trigger (Temporary Solution)

If automatic trigger doesn't work immediately:
1. Click **Build Now** in Jenkins
2. Pipeline will run and deploy changes
3. Continue troubleshooting webhook setup

## Quick Test

Run this to test if everything works:

```bash
# Make a test change
echo "<!-- Test -->" >> app/templates/index.html
git add .
git commit -m "Test auto-deployment"
git push origin main
```

Within 2 minutes (or immediately with webhook), Jenkins should start building!

