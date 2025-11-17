pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/opt/python@3.14:${env.PATH}"
    }
    
    stages {
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up the environment'
                    sh 'python --version'
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    echo 'Building the application'
                    sh 'python scripts/build.py'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    echo 'Running tests'
                    sh 'python scripts/test.py'
                }
            }
            post {
                always {
                    script {
                        echo 'Publishing test results'
                        // Publishing logic here
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying application'
                    sh 'python scripts/deploy.py'
                }
            }
        }
    }
    
    post {
        success {
            script {
                echo 'Pipeline completed successfully'
                sh 'python scripts/notify.py success'
            }
        }
        failure {
            script {
                echo 'Pipeline failed'
                sh 'python scripts/notify.py failure'
            }
        }
    }
}