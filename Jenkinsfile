pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the repository
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/master']], // or the desired branch
                    userRemoteConfigs: [[url: 'https://github.com/saranshverma21345/DevOps.git']]
                ])
            }
        }
        
        stage('Navigate to Folder') {
            steps {
                // Change directory to the desired folder
                dir('/blob/master/scripts/DevOps_Testing.py') {
                    sh 'DevOps_Testing.py'
                    echo 'New File created'
                }
            }
        }
    }
}
