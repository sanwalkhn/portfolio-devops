pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'portfolio-app'
        CONTAINER_NAME = 'portfolio-app-run'
        DOCKER_PORT = '5000'
    }
    
    triggers {
        // Poll GitHub every 2 minutes for changes (as backup)
        pollSCM('H/2 * * * *')
        // GitHub webhook will trigger immediately on push
        // Make sure to enable "GitHub hook trigger for GITScm polling" in job settings
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    sh '''
                        docker build -t ${DOCKER_IMAGE}:latest .
                        docker tag ${DOCKER_IMAGE}:latest ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    '''
                }
            }
        }
        
        stage('Stop Old Container') {
            steps {
                echo 'Stopping old container if running...'
                script {
                    sh '''
                        if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
                            docker stop ${CONTAINER_NAME} || true
                            docker rm ${CONTAINER_NAME} || true
                        fi
                    '''
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying new container...'
                script {
                    sh '''
                        docker run -d \\
                            -p ${DOCKER_PORT}:5000 \\
                            --name ${CONTAINER_NAME} \\
                            --restart unless-stopped \\
                            ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }
        
        stage('Health Check') {
            steps {
                echo 'Checking container health...'
                script {
                    sh '''
                        sleep 5
                        if docker ps | grep -q ${CONTAINER_NAME}; then
                            echo "Container is running successfully!"
                            docker ps | grep ${CONTAINER_NAME}
                        else
                            echo "Container failed to start!"
                            exit 1
                        fi
                    '''
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
            echo "Application deployed at http://localhost:${DOCKER_PORT}"
        }
        failure {
            echo 'Pipeline failed! Check logs for details.'
        }
        cleanup {
            script {
                try {
                    echo 'Cleaning up old images...'
                    sh '''
                        docker image prune -f || true
                    '''
                } catch (Exception e) {
                    echo "Cleanup skipped: ${e.getMessage()}"
                }
            }
        }
    }
}

