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
                    sudo apt-get -y install python3-pip python3-venv ssh
                    python3 -m venv python-env
                    . python-env/bin/activate
                    pip3 install pylint
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
                sh 'ssh ubuntu@54.156.89.92 rm -rf /temp_deploy'
                sh 'ssh ubuntu@54.156.89.92 mkdir -p /temp_deploy'
                sh 'ssh ubuntu@54.156.89.92 ls -la'
                
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
