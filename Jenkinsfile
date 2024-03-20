pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/amitbron612/WorldOfGames.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build('mainscores')
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image('mainscores').withRun('-p 8777:5000 -v $(pwd)/scores.json:/scores.json') { c ->
                        sh 'sleep 10' // Wait for the container to start (adjust as needed)
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'pip install -r requirements.txt' // Install dependencies
                    sh 'python e2e.py' // Run the Selenium tests
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    docker.image('mainscores').remove(force: true) // Remove the container
                    docker.image('mainscores').push() // Push the image to DockerHub
                }
            }
        }
    }
}
