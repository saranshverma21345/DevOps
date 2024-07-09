pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    echo "Current directory: ${pwd()}"
                    sh 'ls /home/saransh-verma/Documents/'
                    sh 'python3 /home/saransh-verma/Documents/DevOps_Testing.py'
                }
            }
        }
    }
}
