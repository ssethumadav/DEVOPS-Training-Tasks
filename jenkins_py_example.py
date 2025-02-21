pipeline {
    agent any
 
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ssethumadav/DEVOPS-Training-Tasks/edit/main.git', branch: 'main'
            }
        }
 
        stage('Set Up Virtual Environment') {
            steps {
                // Ensure python3-venv is available
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate' // Activate the virtual environment
            }
        }
 
        stage('Install Dependencies') {
            steps {
                // Install dependencies inside the virtual environment
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
 
        stage('Run Tests') {
            steps {
                // Run tests inside the virtual environment
                sh '. venv/bin/activate && PYTHONPATH=$PWD pytest test/'
            }
        }
 
        stage('Build Artifact') {
            steps {
                // Build the artifact inside the virtual environment
                sh '. venv/bin/activate && python setup.py sdist'
            }
        }
 
        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }
}
def hello_world():     print("Hello, Worl... by Barathkumar Jangamanayakanpatti Karuppannan(UST,IN)12:53Barathkumar Jangamanayakanpatti Karuppannan(UST,IN)
def hello_world():
    print("Hello, World!")
 
if __name__ == "__main__":
    hello_world()
 from setuptools import setup, find_packages... by Barathkumar Jangamanayakanpatti Karuppannan(UST,IN)12:54Barathkumar Jangamanayakanpatti Karuppannan(UST,IN)
from setuptools import setup, find_packages
 
setup(
    name='python-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
)
 # test_app.py from app import hello_world i... by sethumadav 
# test_app.py
from app import hello_world
import pytest
 
def test_hello_world(capfd):
    hello_world()
    captured = capfd.readouterr()
    assert captured.out == "Hello, World!\n"
 image by sethumadav
 
has context menu
