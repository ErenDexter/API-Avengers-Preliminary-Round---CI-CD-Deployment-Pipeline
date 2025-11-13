pipeline {
    agent any

    environment {
        APP_IMAGE = "demo-app:${env.BUILD_NUMBER ?: 'local'}"
        DOCKER_COMPOSE_FILE = "docker-compose.yml"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Setting up Python dependencies for tests (virtual env)...'
                sh 'python -V || true'
            }
        }

        stage('Build') {
            steps {
                echo 'Running syntax check...'
                sh 'python -m py_compile app/main.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests (mock tests)...'
                sh 'python -m unittest discover -v app'
            }
        }

        stage('Package (Docker)') {
            steps {
                echo "Building Docker image ${APP_IMAGE}..."
                sh "docker build -t ${APP_IMAGE} ."
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application with docker-compose...'
                sh "docker-compose -f ${DOCKER_COMPOSE_FILE} up -d --build app"
            }
        }

        stage('Health Check') {
            steps {
                echo 'Verifying container health...'
                sh 'chmod +x healthcheck.sh || true'
                sh './healthcheck.sh'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up (docker-compose down)'
            sh 'docker-compose down || true'
        }
    }
}
