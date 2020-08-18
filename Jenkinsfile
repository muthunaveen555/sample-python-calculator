pipeline {

    agent any

    stages {

        stage("build") {

            steps{
                echo 'building application..'
                echo 'creating virtual environment'
                sh "pwd"
                sh "ls -la"
            }
        }
        stage("test") {

            steps{
                echo 'testing the application..'
                
            }
        }
        stage("deploy") {

            steps{
                echo 'Deploying the application..'
                
            }
        }
        stage("cleaning workspace"){

            steps{
                echo 'cleaning workspace'
                sh 'rm -rf /var/lib/jenkins/workspace/calculator_pipeline'
		sh 'pwd'
		sh 'ls -la'
            }
        }
    }
}
