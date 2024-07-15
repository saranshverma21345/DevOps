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
                        sh "python3 ${scriptPath}"
                    } else {
                        error "Script not found: ${scriptPath}"
                    }
                }
            }
        }

        stage('Verify Created File') {
            steps {
                script {
                    def createdFilePath = '/var/lib/jenkins/workspace/personal Project_DevOps/CI_VIEW/file.txt' // Adjust according to your Python script

                    if (fileExists(createdFilePath)) {
                        echo "File created by Python script found: ${createdFilePath}"
                        def fileContent = readFile(createdFilePath)
                        echo "File content: ${fileContent}"
                    } else {
                        error "File created by Python script not found: ${createdFilePath}"
                    }
                }
            }
        }
    }
}
