def myflag = false

properties([pipelineTriggers([githubPush()])])

pipeline {

  options {
    timeout(time: 2, unit: 'HOURS')
    gitLabConnection('Gitlab')
  }
  environment {
    DOCKER_REGISTRY='registry.petuum.com/internal/scalable-ml/autodist/toolchain'
  }
    //agent none
    agent {node { label 'petuum-jenkins-slave'}}
    stages {
        stage('print-env') {
            //agent {
            //    label 'GPU2'
            //}
            steps {
                setBuildStatus("Build in progress", "pending", "${env.GIT_COMMIT}", "${env.BUILD_URL}");
                sleep(15)
                sh "printenv" 
            }
        }
        /*
        stage('build-image') {
            agent {
                label 'GPU2'
            }
            steps {
                sh "docker ps" 
            }
        }
        stage('lint') {
            agent {
                docker { 
                    label 'GPU2'
                    image "${DOCKER_REGISTRY}:tf2"
                }
            }
            steps{
                sh 'prospector sampleapp'
            }
        }
        */
    }

    post {
        success {
            setBuildStatus("Build succeeded", "success", "${env.GIT_COMMIT}", "${env.BUILD_URL}");
        }
        failure {
            setBuildStatus("Build failed", "failure", "${env.GIT_COMMIT}", "${env.BUILD_URL}");
        }
    }
}

// We've disabled the github commit notification from plugin because it doesn't
// allow us to overwrite the target URL (it takes raw hostname of jenkins server,
// which we dont want, as we're pointing to public hostname instead.
//
// In future, we can use setBuildStatusViaPlugin() instead, but until those plugins
// become more stable, can use this.
void setBuildStatus(String message, String state, String gitCommit, String buildUrl) {
    withCredentials([string(credentialsId: 'github-service-token', variable: 'TOKEN')]) 
    {
        String statusUrl = "https://api.github.com/repos/schahal/sample/statuses/$gitCommit"
        String targetUrl = buildUrl.replaceAll(/http.*\.(com|io)\//,"https://jenkins.petuum.io/")
        print("targetUrl is "+targetUrl)

        // 'set -x' for debugging. Don't worry the access token won't be actually logged
        // Also, the sh command actually executed is not properly logged, it will be further escaped when written to the log
        sh """
            set -x
            curl -H \"Authorization: token $TOKEN\" \
                 -X POST \
                 -d '{\"description\": \"$message\", \"state\": \"$state\", \"context\": "ci/jenkins", \"target_url\" : \"$targetUrl\" }' ${statusUrl}
        """
    }
}

// Don't use this until plugins become more stable, for example:
// https://issues.jenkins-ci.org/browse/JENKINS-54249.
// 
// Instead, opt for setBuildStatus() and disable from job (we need to send 
// our own notification because auto won't allow us to set the public revere proxy URL
void setBuildStatusViaPlugin(String message, String state, String gitCommit, String repoSource) {
  step([
      $class: "GitHubCommitStatusSetter",
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/branch"],
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: repoSource],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "error"]],
      statusBackrefSource: [$class: "ManuallyEnteredBackrefSource", backref: "http://52.26.133.24:8080/job/Arion/"],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}
