pipeline {
  agent any

  environment {
    IMAGE_NAME = "abkaur/webapp"
    TAG = "${BUILD_NUMBER}"
    DEPLOY_REPO = "https://github.com/abkaur/webapp-deploy.git"
  }

  stages {

    stage('Checkout App Code') {
      steps {
        git url: 'https://github.com/abkaur/webapp.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${IMAGE_NAME}:${TAG} ."
      }
    }

    stage('Trivy Image Scan') {
      steps {
        sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin'
        sh "trivy image ${IMAGE_NAME}:${TAG}"
      }
    }

    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh """
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push ${IMAGE_NAME}:${TAG}
          """
        }
      }
    }

    stage('Update Deployment Repo') {
      steps {
        withCredentials([string(credentialsId: 'GITHUB_TOKEN', variable: 'TOKEN')]) {
          sh '''
            git clone https://${TOKEN}@github.com/abkaur/webapp-deploy.git
            cd webapp-deploy/k8s
            sed -i "s|image: .*|image: abkaur/webapp:${BUILD_NUMBER}|" deployment.yaml
            git config user.name "Jenkins"
            git config user.email "jenkins@ci.local"
            git commit -am "Updated image tag to ${BUILD_NUMBER}"
            git push
          '''
        }
      }
    }
  }
}
