pipeline {
  agent any

  environment {
    VENV_DIR = ".venv"
    DOCKER_IMAGE = "docker.io/swaroop3/spe-calculator"
    IMAGE_TAG = "${env.IMAGE_TAG ?: env.BUILD_NUMBER}"
  }

  options {
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        sh 'python3 -m venv ${VENV_DIR}'
        sh '. ${VENV_DIR}/bin/activate && pip install --upgrade pip'
        sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
      }
    }

    stage('Lint') {
      steps {
        sh '. ${VENV_DIR}/bin/activate && ruff check spe_calculator tests'
      }
    }

    stage('Unit Tests') {
      steps {
        sh 'mkdir -p reports'
        sh '. ${VENV_DIR}/bin/activate && pytest --junitxml=reports/pytest.xml'
      }
      post {
        always {
          junit 'reports/pytest.xml'
        }
      }
    }

    stage('Build Package') {
      steps {
        sh 'rm -rf dist && mkdir -p dist'
        sh '. ${VENV_DIR}/bin/activate && python -m build'
        archiveArtifacts artifacts: 'dist/*', fingerprint: true, allowEmptyArchive: false
      }
    }

    stage('Build Image') {
      steps {
        script {
          env.FULL_IMAGE = "${env.DOCKER_IMAGE}:${env.IMAGE_TAG}"
        }
        sh 'docker build -t ${FULL_IMAGE} .'
      }
    }

    stage('Push Image') {
      when {
        expression {
          return env.DOCKERHUB_CREDENTIALS?.trim()
        }
      }
      steps {
        withCredentials([
          usernamePassword(
            credentialsId: env.DOCKERHUB_CREDENTIALS,
            usernameVariable: 'DOCKERHUB_USER',
            passwordVariable: 'DOCKERHUB_PASS'
          )
        ]) {
          sh 'echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin'
          sh 'docker push ${FULL_IMAGE}'
        }
      }
    }

    stage('Deploy via Ansible') {
      when {
        allOf {
          expression { fileExists('scripts/deploy_with_ansible.sh') }
          expression { sh(script: 'command -v ansible-playbook >/dev/null 2>&1', returnStatus: true) == 0 }
        }
      }
      steps {
        sh 'chmod +x scripts/deploy_with_ansible.sh'
        sh 'scripts/deploy_with_ansible.sh --extra-vars "calculator_image=${FULL_IMAGE}"'
      }
    }
  }

  post {
    always {
      script {
        sh(script: 'docker logout', returnStatus: true)
      }
    }
  }
}
