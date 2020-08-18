pipeline {

    agent any

    stages {

        stage("cleaning ec2 instance") {

            steps{
                echo 'cleaning the directory..'
                echo 'before cleaning..'
                sh 'ssh ubuntu@54.156.89.92 ls -la'
                sh 'ssh ubuntu@54.156.89.92 rm -rf temp_deploy'
                echo 'After cleaning..'
                sh 'ssh ubuntu@54.156.89.92 ls -la'
            }
        }
        
        stage("build") {

            steps{
                echo 'building application..'
                echo 'creating virtual environment'
                sh "pwd"
                sh """
                    sudo apt-get -y install python3-pip python3-venv ssh
                    sudo touch app/history.txt
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
                echo 'removing previous deployed directory..'
                sh 'ssh ubuntu@54.156.89.92 rm -rf temp_deploy'
                echo 'create new deploy directory..'
                sh 'ssh ubuntu@54.156.89.92 mkdir -p temp_deploy'
                sh 'scp -r /var/lib/jenkins/workspace/python-virtual-env-pipeline ubuntu@54.156.89.92:/home/ubuntu/temp_deploy/'
                echo 'After moving files into ec2 instance'
                sh 'ssh ubuntu@54.156.89.92 ls -la'
                sh 'ssh ubuntu@54.156.89.92 touch temp_deploy/python-virtual-env-pipeline/app/history.txt'
                echo 'Running test application..'
                sh """
                    ssh ubuntu@54.156.89.92 python3 temp_deploy/python-virtual-env-pipeline/app/test_in_remote_calculator.py
                    """ /*ssh ubuntu@54.156.89.92 python3 calculator.py*/
                
            }
        }
    }
     post {
        always {
            echo 'cleaning workspace..'
            echo 'Current workspace directory'
            sh 'pwd'
            echo 'Before cleaning workspace directory'
            sh 'ls -la'
            deleteDir() /* clean up our workspace */
            echo 'After cleaning workspace directory'
            sh 'ls -la'
        }
    }
}
