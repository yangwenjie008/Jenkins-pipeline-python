pipeline {
    agent any



    environment {
        PATH = "/usr/bin/python3:$PATH"
    }
    
    stages {
             stage('Environment Check') {
            steps {
                sh '''
                    echo "Current PATH:"
                    echo $PATH
                    
                    echo "Home directory:"
                    echo $HOME
                    
                    echo "Who am I:"
                    whoami
                    
                    echo "Python3 location:"
                    which python3
                    
                    echo "Available Python versions:"
                    ls -la /usr/bin/python*
                '''
            }
        }
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up the environment'
                    sh 'python3 --version'
                }
            }
        }
        
        stage('Build') {
            steps {
                script {
                    echo 'Building the application'
                    sh 'python3 scripts/build.py'
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