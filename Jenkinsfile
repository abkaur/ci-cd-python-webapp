pipeline {
  agent any

  environment {
    IMAGE_NAME = "abkaur95/webapp"
    TAG = "${BUILD_NUMBER}"
    DEPLOY_REPO = "https://github.com/abkaur/webapp-deploy.git"
    SONAR_HOST_URL = "http://34.58.130.72:9000"
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

    stage('SonarQube Analysis') {
      steps {
        withCredentials([string(credentialsId: 'SONAR_TOKEN', variable: 'SONAR_TOKEN')]) {
          sh """
            curl -sSLo sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
            unzip sonar-scanner.zip
            ./sonar-scanner-*/bin/sonar-scanner \
              -Dsonar.projectKey=webapp \
              -Dsonar.sources=webapp \
              -Dsonar.host.url=${SONAR_HOST_URL} \
              -Dsonar.login=${SONAR_TOKEN}
          """
        }
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
          sh """
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push ${IMAGE_NAME}:${TAG}
          """
        }
      }
    }

    stage('Update Deployment Repo') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
          sh '''
            git clone https://${GIT_USER}:${GIT_PASS}@github.com/abkaur/webapp-deploy.git
            cd webapp-deploy/k8s
            sed -i "s|image: .*|image: abkaur95/webapp:${BUILD_NUMBER}|" deployment.yaml
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
