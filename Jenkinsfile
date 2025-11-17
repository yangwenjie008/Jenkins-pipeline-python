pipeline {
    agent any



    environment {
        PATH = "/usr/bin/python3:${env.PATH}"
    }
    
    stages {
        stage('Setup') {
            steps {
                script {
                    sh 'PATH'
                    echo 'Setting up the environment'
                    sh 'python3 --version'
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
                    sh 'python3 scripts/test.py'
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
                    sh 'python3 scripts/deploy.py'
                }
            }
        }
    }
    
    post {
        success {
            script {
                echo 'Pipeline completed successfully'
                sh 'python3 scripts/notify.py success'
            }
        }
        failure {
            script {
                echo 'Pipeline failed'
                sh 'python3 scripts/notify.py failure'
            }
        }
    }
}