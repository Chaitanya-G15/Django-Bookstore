pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'bookstore-image'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo '✅ Cloning repository...'
                // Jenkins will clone repo by default; no need to do anything
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run Migrations') {
            steps {
                sh "docker-compose run web python manage.py migrate"
            }
        }

        stage('Run Server') {
            steps {
                sh "docker-compose up -d"
            }
        }
    }

    post {
        success {
            echo '✅ Deployment completed successfully!'
        }
        failure {
            echo '❌ Deployment failed!'
        }
    }
}
