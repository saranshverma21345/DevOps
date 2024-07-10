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
                dir('/DevOps/blob/master/scripts/DevOps_Testing.py') {
                    // Here you can add further steps to build/test/deploy
                    echo 'Now in the desired folder'
                }
            }
        }
