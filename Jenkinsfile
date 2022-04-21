pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t teucer12/helloWorld-2022 .'
                sh 'docker run -d -p 10243:10243 --name helloWorld teucer12/helloWorld-2022'
            }
        }
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
        stage('Cleanup') {
                    steps {
                sh 'docker stop helloWorld'
                sh 'docker rm helloWorld'
                }
            }

    }
    post {
        always {
                echo 'This will always run'
            }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
