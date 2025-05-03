pipeline {
  agent any

  environment {
    IMAGE_NAME = "abkaur95/webapp"
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
        sh '''
          mkdir -p ./bin
          curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b ./bin
          ./bin/trivy image ${IMAGE_NAME}:${TAG}
        '''
      }
    }

    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --

