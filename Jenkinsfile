pipeline {
    agent { docker { image 'Jenkinsfile_Docker_App_Image()' } }
    stages {
        stage('install') {
            steps {

                sh sudo python -m pip install --upgrade pip 
                sh sudo pip install --upgrade pip
                sh sudo pip install pipenv
                sh sudo pipenv install
                sh sudo pipenv install Django==2.2
                sh sudo pipenv install pytest-django
            }
            
        stage('build') {
            steps {
      

                sh [ $EUID == 0 ] && SUDO=" || SUDO=sudo && $SUDO chown -R circleci:circleci /usr/local/bin
                sh [ $EUID == 0 ] && SUDO=" || SUDO=sudo && $SUDO chown -R circleci:circleci /usr/local/lib/python3.7/site-packages
                sh sudo pipenv run pytest --junitxml=test-results/junit.xml djangodemo/tests
                sh sudo python djangodemo/setup.py sdist
            }
        }
    }
}
