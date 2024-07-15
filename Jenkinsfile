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

        stage('Read File') {
            steps {
                script {
                    // Define the path to the file relative to the repo root
                    def filePath = 'scripts/DevOps_Testing.py'
                    
                    // Check if the file exists
                    if (fileExists(filePath)) {
                        echo "File found: ${filePath}"

                        sh "python3 $(scripts/DevOps_Testing.py)"
                        
                        // Read the file content
                        def fileContent = readFile(filePath)
                        echo "File content: ${fileContent}"
                    } else {
                        error "File not found: ${filePath}"
                    }
                }
            }
        }
    }
}
