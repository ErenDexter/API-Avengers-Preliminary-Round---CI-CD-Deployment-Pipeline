pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building application (simple syntax check)...'
                sh 'python -m py_compile app/main.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running mock unit tests...'
                sh 'python app/test.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t app:latest .'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo 'Starting application via docker-compose...'
                sh 'docker-compose up -d'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Running healthcheck script...'
                sh 'chmod +x healthcheck.sh'
                sh './healthcheck.sh'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker-compose down || true'
        }
    }
}
