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
    }
    post {
        always {
            echo 'cleaning workspace..'
            deleteDir() /* clean up our workspace */
            sh 'pwd'
            sh 'ls -la'
        }
    }
}
