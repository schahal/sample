def myflag = false

pipeline {
  options {
    timeout(time: 2, unit: 'HOURS')
  }
  environment {
    DOCKER_REGISTRY='registry.petuum.com/internal/scalable-ml/autodist/toolchain'
  }
    agent none
    stages {
        stage('build-image') {
            agent {
                label 'GPU1'
            }
            steps {
                sh "docker ps" 
            }
        }
        stage('lint') {
            agent {
                docker { 
                    label 'GPU1'
                    image "${DOCKER_REGISTRY}:tf2"
                }
            }
            steps{
                sh 'prospector sampleapp'
            }
        }
    }
}
