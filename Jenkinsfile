pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/master']], // or the desired branch
                    userRemoteConfigs: [[url: 'https://github.com/saranshverma21345/DevOps.git']]
                ])
            }
        }

        stage('Print Workspace Directory') {
            steps {
                script {
                    def workspace = pwd()
                    echo "Workspace directory: ${workspace}"
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    def scriptPath = 'scripts/DevOps_Testing.py'
                    
                    if (fileExists(scriptPath)) {
                        echo "Script found: ${scriptPath}"
                        sh 'sudo install pandas'
                        sh "python3 ${scriptPath}"
                    } else {
                        error "Script not found: ${scriptPath}"
                    }
                }
            }
        }
    }
}


                
