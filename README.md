# DevOps Trio Portfolio

A modern portfolio website built with Flask, Docker, and automated CI/CD using Jenkins.

## Features

- 🎨 Modern UI with enhanced gradient colors and animations
- 🐳 Dockerized application
- 🔄 Automated CI/CD pipeline with Jenkins
- 📦 Containerized deployment

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Containerization:** Docker
- **CI/CD:** Jenkins

## Setup Instructions

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/sanwalkhn/portfolio-devops.git
cd portfolio-devops
```

2. Run with Docker:
```bash
docker build -t portfolio-app .
docker run -d -p 5000:5000 --name portfolio-app-run portfolio-app
```

3. Access the application:
```
http://localhost:5000
```

### Jenkins CI/CD Setup

#### 1. Create Jenkins Pipeline Job

1. Open Jenkins dashboard
2. Click **New Item**
3. Enter job name (e.g., `portfolio-devops`)
4. Select **Pipeline** and click **OK**

#### 2. Configure Pipeline

1. In **Pipeline** section:
   - **Definition:** Pipeline script from SCM
   - **SCM:** Git
   - **Repository URL:** `https://github.com/sanwalkhn/portfolio-devops.git`
   - **Branch:** `*/main`
   - **Script Path:** `Jenkinsfile`

#### 3. Enable GitHub Webhook (Automatic Trigger)

**Option A: Using GitHub Webhook (Recommended)**

1. In Jenkins job configuration:
   - Go to **Build Triggers** section
   - Check **GitHub hook trigger for GITScm polling**

2. In GitHub repository:
   - Go to **Settings** → **Webhooks** → **Add webhook**
   - **Payload URL:** `http://your-jenkins-server:8080/github-webhook/`
   - **Content type:** `application/json`
   - **Events:** Select **Just the push event**
   - Click **Add webhook**

**Option B: Using Poll SCM (Already configured)**

The Jenkinsfile already includes poll SCM that checks every minute. No additional setup needed.

#### 4. Configure Jenkins User Permissions

Make sure Jenkins user has Docker permissions:
```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

#### 5. Run Pipeline

1. Click **Build Now** to test the pipeline
2. After successful setup, every push to GitHub will automatically:
   - Build Docker image
   - Stop old container
   - Deploy new container
   - Run health checks

## Pipeline Stages

1. **Checkout** - Pulls latest code from GitHub
2. **Build Docker Image** - Builds the Docker image
3. **Stop Old Container** - Stops and removes old container
4. **Deploy** - Runs new container with latest changes
5. **Health Check** - Verifies container is running

## Project Structure

```
.
├── app/
│   ├── static/
│   │   └── style.css      # Enhanced CSS with gradients
│   ├── templates/
│   │   ├── index.html
│   │   ├── projects.html
│   │   └── contact.html
│   └── app.py             # Flask application
├── Dockerfile             # Docker configuration
├── Jenkinsfile            # CI/CD pipeline
├── requirements.txt        # Python dependencies
└── README.md
```

## Team

- Sanwal Afraiz
- Muhammad Abdullah Khan
- Ahmad Ali

## License

© 2025 DevOps Trio - All Rights Reserved

