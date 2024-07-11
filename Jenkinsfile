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
                script{
                def filePath ='/DevOps/blob/master/scripts/DevOps_Testing.py' {
                    sh 'DevOps_Testing.py'
                    echo 'New File created'
                }
            }
        }
    }
}
}
