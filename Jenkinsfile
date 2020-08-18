pipeline {

    agent any

    stages {

        stage("build") {

            steps{
                echo 'building application..'
                echo 'creating virtual environment'
                sh "pwd"
                sh "ls -la"
                sh """
                    sudo apt-get -y install python3-pip
                    sudo pip3 install virtualenv
                    sudo virtualenv python-env
                    sudo source python-env/bin/activate
                    sudo pip3 install pylint
                    """
            }
        }

        stage("linting-score") {

            steps{
                echo 'Linting the application..'
                sh 'python3 -m pylint app/calculator.py'

            }
        }

        stage("test") {

            steps{
                echo 'testing the application..'
                sh 'python3 -m unittest discover -v'
                
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
