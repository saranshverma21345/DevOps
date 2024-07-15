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

        stage('Run Python Script') {
            steps {
                script {
                    // Define the path to the Python script relative to the repo root
                    def scriptPath = 'scripts/DevOps_Testing.py'
                    
                    // Check if the script exists
                    if (fileExists(scriptPath)) {
                        echo "Script found: ${scriptPath}"
                        
                        // Run the Python script
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
                    // Define the path to the file created by the Python script
                    def createdFilePath = '/scripts' // Adjust according to your Python script

                    // Check if the file exists
                    if (fileExists(createdFilePath)) {
                        echo "File created by Python script found: ${createdFilePath}"
                        
                        // Read and print the file content
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
