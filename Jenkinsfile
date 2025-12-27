pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "hotel-prediction:${BUILD_NUMBER}"
        DOCKER_LATEST = "hotel-prediction:latest"
        GITHUB_REPO = 'https://github.com/Tejesh0209/HotelReservationPrediction.git'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repository..."
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo "Setting up Python virtual environment..."
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh '''
                    . venv/bin/activate
                    pip install --no-cache-dir -r requirements.txt
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh '''
                    docker build -t ${DOCKER_IMAGE} -t ${DOCKER_LATEST} -f custom_jenkins/Dockerfile .
                '''
            }
        }
        
        stage('Test Application') {
            steps {
                echo "Testing Docker image..."
                sh '''
                    docker images | grep hotel-prediction
                '''
            }
        }
        
        stage('Push to Registry') {
            steps {
                echo "Docker image ready: ${DOCKER_LATEST}"
                sh '''
                    echo "Image: ${DOCKER_LATEST}"
                    echo "To run locally: docker run -p 8080:8080 ${DOCKER_LATEST}"
                '''
            }
        }
    }
    
    post {
        success {
            echo "Pipeline completed successfully!"
            echo "Docker image available as: ${DOCKER_LATEST}"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
        always {
            echo "Pipeline execution finished."
        }
    }
}
