# Hotel Reservation Cancellation Prediction

A complete machine learning solution for predicting hotel reservation cancellations using LightGBM, with Flask web interface and automated CI/CD deployment via Jenkins and Docker.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Deployment](#deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)

---

## Problem Statement

Objective: Predict whether a hotel reservation will be cancelled or not.

Context: Hotel cancellations impact revenue management, planning, and operational efficiency. Early prediction of cancellations enables hotels to:
- Implement targeted retention strategies
- Optimize room inventory
- Plan staffing and resources effectively
- Minimize revenue loss

Dataset: Hotel reservation data with 10 key features:
- Lead time (days between booking and arrival)
- Number of special requests
- Average price per room
- Arrival month and date
- Market segment type
- Number of week and weekend nights
- Type of meal plan
- Room type reserved

Target Variable: Binary classification - Canceled (1) or Not Canceled (0)

---

## Solution Overview

This project implements an end-to-end machine learning pipeline:

1. Data Ingestion - Load raw hotel reservation data from Google Cloud Storage
2. Data Processing - Clean, transform, and engineer features
3. Model Training - Train LightGBM with hyperparameter optimization
4. Web Interface - Flask app for real-time predictions
5. Containerization - Docker for reproducible deployments
6. CI/CD - Jenkins pipeline for automated testing and deployment

Key Achievements

- Model Accuracy: 90.67%
- Precision: 90.68%
- Recall: 90.67%
- F1-Score: 90.66%

---

## Project Architecture

```
Google Cloud Storage (Raw Data 3.1 MB)
                    |
                    v
Data Pipeline (Ingestion, Processing, Feature Engineering)
                    |
                    v
Model Training (LightGBM with Hyperparameter Optimization)
                    |
                    v
Flask Web Application (Prediction Interface)
                    |
        ____________|____________
       |                         |
       v                         v
Local Testing            Jenkins CI/CD Pipeline
                         (Checkout -> Install -> Build -> Test -> Deploy)
                         |
                         v
                    Docker Container
                    (Production Ready)
                    |
                    v
        Cloud Deployment (Google Cloud Run/Compute Engine)
```

---

## Tech Stack

Core ML & Data Processing
- Python 3.12 - Primary programming language
- pandas 2.3.3 - Data manipulation
- numpy 1.26.4 - Numerical computing
- scikit-learn 1.8.0 - Machine learning
- LightGBM 4.6.0 - Gradient boosting framework
- XGBoost 3.1.2 - Alternative boosting algorithm
- imbalanced-learn - Handle class imbalance with SMOTE
- joblib 1.5.3 - Model serialization

Web Framework
- Flask 3.1.2 - Web application framework
- Gunicorn 23.0.0 - Production WSGI server
- Jinja2 - Template rendering

Cloud & Data Storage
- Google Cloud Storage (GCS) - Data hosting
- google-cloud-storage - Python client

DevOps & Containerization
- Docker - Containerization
- Jenkins 2.528.3 LTS - CI/CD automation
- Groovy - Jenkins pipeline language

Experiment Tracking
- MLflow 3.8.0 - Experiment tracking and model registry

Utilities
- pyyaml 6.0 - YAML configuration
- statsmodels - Statistical analysis
- matplotlib & seaborn - Data visualization

---

## Project Structure

```
HotelReservationPrediction/
├── README.md                          (This file)
├── requirements.txt                   (Python dependencies)
├── setup.py                          (Package setup)
├── Jenkinsfile                       (Jenkins CI/CD pipeline)
├── docker-compose.yml                (Docker multi-container setup)
│
├── app.py                            (Flask web application)
├── config/                           (Configuration files)
│   ├── paths_config.py              (File path definitions)
│   └── model_params.py              (ML model hyperparameters)
│
├── src/                              (Source code)
│   ├── __init__.py
│   ├── logger.py                    (Logging configuration)
│   ├── custom_exception.py          (Custom exception handling)
│   └── model_training.py            (Model training logic)
│
├── pipeline/                         (ML pipeline orchestration)
│   ├── data_ingestion.py            (Load data from GCS)
│   ├── data_processing.py           (Feature engineering & preprocessing)
│   ├── training_pipeline.py         (End-to-end pipeline coordinator)
│   └── predict.py                   (Prediction utility)
│
├── utils/                            (Utility functions)
│   ├── __init__.py
│   └── common_functions.py          (Shared helper functions)
│
├── artifacts/                        (Model & processed data)
│   ├── models/
│   │   └── best_model.pkl           (Trained LightGBM model - 35 MB)
│   ├── processed_data/
│   │   ├── train.csv
│   │   └── test.csv
│   └── raw_data/
│
├── templates/                        (HTML templates)
│   └── index.html                   (Prediction form & results)
│
├── static/                           (Static files)
│   └── style.css                    (CSS styling)
│
├── notebook/                         (Jupyter notebooks)
│   └── model_exploration.ipynb      (EDA & model comparison)
│
├── custom_jenkins/                   (Docker configuration)
│   ├── Dockerfile                   (Flask app container)
│   └── Dockerfile.jenkins           (Jenkins container with Docker)
│
├── logs/                            (Application logs)
├── mlruns/                          (MLflow experiment tracking)
└── venv/                            (Python virtual environment)
```

---

## Setup & Installation

Prerequisites

- Python 3.12+ - Download here
- Docker - Install Docker
- Google Cloud Account - For GCS data access
- Jenkins (optional) - For CI/CD

Step 1: Clone Repository

```bash
git clone https://github.com/Tejesh0209/HotelReservationPrediction.git
cd HotelReservationPrediction
```

Step 2: Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Step 4: Configure Google Cloud Authentication

```bash
# Set up Google Cloud credentials
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"

# Verify authentication
gcloud auth application-default login
```

Step 5: Run Data Pipeline

```bash
# Execute complete ML pipeline
python pipeline/training_pipeline.py
```

This will:
1. Download data from Google Cloud Storage
2. Process and engineer features
3. Train LightGBM model
4. Save model to artifacts/models/best_model.pkl

---

## Usage

Local Web Application

```bash
# Start Flask development server
python app.py
```

Visit http://localhost:5000 in your browser.

Using the App:
1. Enter hotel reservation details in the form:
   - Lead time (days)
   - Number of special requests
   - Average price per room
   - Arrival month and date
   - Market segment type (1-4)
   - Number of week and weekend nights
   - Meal plan type (1-5)
   - Room type (1-7)

2. Click "Predict" to get cancellation prediction

3. Result displays as:
   - Canceled - Reservation likely to be cancelled
   - Not Canceled - Reservation likely to be completed

Production Deployment with Gunicorn

```bash
# Run with Gunicorn (4 workers)
gunicorn --workers 4 --bind 0.0.0.0:8080 app:app
```

Command Line Prediction

```python
from pipeline.predict import predict_cancellation

features = {
    'lead_time': 342,
    'no_of_special_requests': 1,
    'avg_price_per_room': 110.0,
    'arrival_month': 7,
    'arrival_date': 1,
    'market_segment_type': 1,
    'no_of_week_nights': 1,
    'no_of_weekend_nights': 2,
    'type_of_meal_plan': 1,
    'room_type_reserved': 1
}

prediction = predict_cancellation(features)
print(f"Prediction: {prediction}")  # Output: 'Canceled' or 'Not_Canceled'
```

---

## Model Performance

Model Metrics

| Metric | Value |
|--------|-------|
| Accuracy | 90.67% |
| Precision | 90.68% |
| Recall | 90.67% |
| F1-Score | 90.66% |

Model Configuration

- Algorithm: LightGBM (Gradient Boosting)
- Number of Leaves: 31
- Learning Rate: 0.1
- Number of Estimators: 100
- Subsample Ratio: 0.8
- Optimization Metric: F1-score (weighted average)
- Class Balancing: SMOTE applied to handle class imbalance
- Train/Test Split: 80/20
- Hyperparameter Optimization: RandomizedSearchCV

Training Configuration:
- Test split: 80/20
- Class balancing: SMOTE applied
- Optimization metric: F1-score (weighted)

---

##  Deployment

### Docker Deployment

#### Build Docker Image

```bash
# Build Flask application container
docker build -t hotel-prediction:latest -f custom_jenkins/Dockerfile .

# Run container
docker run -d -p 8080:8080 \
  --name hotel-app \
  hotel-prediction:latest
```

Access the app at `http://localhost:8080`

#### Docker Compose (Multi-container)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f jenkins

# Stop all services
docker-compose down
```

**Services:**
- `jenkins` - CI/CD automation (port 8080)
- `hotel-app` - Flask application (port 8081)

---

##  CI/CD Pipeline

### Jenkins Setup

#### Prerequisites

```bash
# Ensure Docker is running
docker --version
```

#### Start Jenkins

```bash
# Using docker-compose (recommended)
docker-compose up -d jenkins

# Or manually
docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```

#### Initialize Jenkins

1. Navigate to `http://localhost:8080`
2. Retrieve initial admin password:
   ```bash
   docker logs jenkins-hotel | grep "Initial admin password"
   ```
3. Install recommended plugins
4. Create admin user
5. Configure GitHub webhook integration

#### Pipeline Stages

The `Jenkinsfile` defines an automated pipeline with 7 stages:

| Stage | Action |
|-------|--------|
| **Checkout** | Clone repository from GitHub |
| **Setup Environment** | Verify Python and dependencies |
| **Install Dependencies** | Install requirements.txt packages |
| **Build Docker Image** | Build Docker image using Dockerfile |
| **Run Tests** | Execute test suite |
| **Push to Registry** | Push image to Docker registry (optional) |
| **Deploy** | Deploy container to production |

**Trigger:** Automatically on GitHub push or manual Jenkins trigger

### GitHub Integration

#### Set Up Webhook

1. Go to GitHub repository Settings → Webhooks
2. Add webhook:
   - **Payload URL:** `http://your-jenkins-server:8080/github-webhook/`
   - **Content type:** `application/json`
   - **Events:** Push events
   - **Active:** ✓

3. Jenkins will automatically trigger builds on code push

#### Configure Jenkins GitHub Credentials

1. Jenkins Dashboard → Manage Jenkins → Credentials
2. Add GitHub personal access token (PAT)
3. Configure pipeline to use credentials

### Manual Trigger

```bash
# Trigger Jenkins build from command line
curl -X POST http://localhost:8080/job/HotelReservation/build \
  -H "Authorization: Bearer <API_TOKEN>"
```

---

## Google Cloud Deployment

### Deploy to Google Cloud Run

#### Prerequisites

```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash

# Initialize
gcloud init

# Set project
gcloud config set project YOUR_PROJECT_ID
```

#### Build and Deploy

```bash
# Authenticate Docker to GCR
gcloud auth configure-docker

# Build and push image
docker build -t gcr.io/YOUR_PROJECT_ID/hotel-prediction:latest .
docker push gcr.io/YOUR_PROJECT_ID/hotel-prediction:latest

# Deploy to Cloud Run
gcloud run deploy hotel-prediction \
  --image gcr.io/YOUR_PROJECT_ID/hotel-prediction:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1
```

#### Set Environment Variables

```bash
gcloud run services update hotel-prediction \
  --set-env-vars="GOOGLE_APPLICATION_CREDENTIALS=/secrets/credentials.json"
```

#### Access Deployed Service

```bash
# Get service URL
gcloud run services describe hotel-prediction --region us-central1
```

Visit the URL in your browser to use the application.

### Deploy to Compute Engine

```bash
# Create VM instance
gcloud compute instances create hotel-prediction-vm \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --machine-type=e2-medium \
  --zone=us-central1-a

# SSH into VM
gcloud compute ssh hotel-prediction-vm --zone=us-central1-a

# On VM: Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Pull and run image
sudo docker run -d -p 80:8080 \
  gcr.io/YOUR_PROJECT_ID/hotel-prediction:latest

# Access at http://EXTERNAL_IP
```

---

## Testing

### Run Unit Tests

```bash
# Execute test suite
python -m pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Integration Tests

```bash
# Test data pipeline
python pipeline/training_pipeline.py

# Test Flask app
python -m pytest tests/test_app.py -v

# Test model predictions
python -m pytest tests/test_predictions.py -v
```

### Docker Testing

```bash
# Build and test image
docker build -t hotel-prediction:test .
docker run -p 8080:8080 hotel-prediction:test

# In another terminal: test endpoint
curl -X POST http://localhost:8080/ \
  -d "lead_time=100&no_of_special_request=1&avg_price_per_room=100"
```

---

## Monitoring & Logging

### Application Logs

Logs are saved to `logs/` directory with rotating file handler:

```bash
# View application logs
tail -f logs/app.log

# View pipeline logs
tail -f logs/pipeline.log
```

### MLflow Tracking

Access MLflow UI to track experiments:

```bash
# Start MLflow UI
mlflow ui

# Visit http://localhost:5000
```

Monitor:
- Model training runs
- Hyperparameter configurations
- Metrics and performance
- Model artifacts

### Docker Logs

```bash
# View Flask app logs
docker logs hotel-prediction-app -f

# View Jenkins logs
docker logs jenkins-hotel -f

# View all services
docker-compose logs -f
```

---

##  Contributing

### Development Setup

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Install dev dependencies: `pip install -r requirements.txt`
4. Make changes and test locally
5. Commit with clear messages: `git commit -m 'Add amazing feature'`
6. Push to branch: `git push origin feature/amazing-feature`
7. Open Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and DRY

---

## License

This project is licensed under the MIT License - see LICENSE file for details.

---

## Support

For questions or issues:

1. **Check existing issues** - [GitHub Issues](https://github.com/Tejesh0209/HotelReservationPrediction/issues)
2. **Create new issue** with detailed description
3. **Contact maintainer** - Tejesh Boppana

---

##  Future Enhancements

- [ ] Add ensemble model combining multiple algorithms
- [ ] Implement real-time data streaming pipeline
- [ ] Add customer segmentation analysis
- [ ] Deploy recommendation engine for retention strategies
- [ ] Add API authentication and rate limiting
- [ ] Implement model A/B testing framework
- [ ] Add feature importance explanations (SHAP/LIME)
- [ ] Multi-language support for web interface

---

## References

- [LightGBM Documentation](https://lightgbm.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Google Cloud Storage Docs](https://cloud.google.com/storage/docs)
- [Jenkins Best Practices](https://www.jenkins.io/doc/)
- [Docker Documentation](https://docs.docker.com/)

---

**Last Updated:** December 2025  
**Version:** 1.0.0  
**Status:** Production Ready 
