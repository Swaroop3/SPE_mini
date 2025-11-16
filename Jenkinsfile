pipeline {
  agent any

  environment {
    VENV_DIR = ".venv"
    DOCKER_IMAGE = "docker.io/swaroop4/spe-calculator"
    IMAGE_TAG = "${env.IMAGE_TAG ?: env.BUILD_NUMBER}"
    DOCKERHUB_CREDENTIALS = "dockerhub"
    DOCKER_HOST = "unix:///var/run/docker.sock"
  }

  options {
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        deleteDir()
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        sh '''
          rm -rf ${VENV_DIR}
          python3 -m venv ${VENV_DIR}
          ${VENV_DIR}/bin/python -m ensurepip --upgrade
          ${VENV_DIR}/bin/python -m pip install --upgrade pip
          ${VENV_DIR}/bin/python -m pip install -r requirements.txt
        '''
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
        withEnv(["DOCKER_HOST=${env.DOCKER_HOST}"]) {
          sh 'docker --version'
          sh 'docker build -t ${FULL_IMAGE} .'
          sh 'docker tag ${FULL_IMAGE} ${DOCKER_IMAGE}:latest'
        }
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
          withEnv(["DOCKER_CONFIG=${env.WORKSPACE}/.docker"]) {
            sh 'mkdir -p "${DOCKER_CONFIG}"'
            sh 'echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin'
            sh 'docker push ${FULL_IMAGE}'
            sh 'docker push ${DOCKER_IMAGE}:latest'
          }
        }
      }
    }

    stage('Deploy via Ansible') {
      when {
        allOf {
          expression { fileExists('scripts/deploy_with_ansible.sh') }
          expression { sh(script: '. ${VENV_DIR}/bin/activate && command -v ansible-playbook >/dev/null 2>&1', returnStatus: true) == 0 }
        }
      }
      steps {
        sh 'chmod +x scripts/deploy_with_ansible.sh'
        script {
          def extraVars = "calculator_image=${FULL_IMAGE} project_root=${env.WORKSPACE} build_from_source=false"
          sh """
            . ${VENV_DIR}/bin/activate
            scripts/deploy_with_ansible.sh --extra-vars '${extraVars}'
          """
        }
      }
    }
  }

  post {
    always {
      script {
        withEnv(["DOCKER_CONFIG=${env.WORKSPACE}/.docker"]) {
          sh(script: 'docker logout >/dev/null 2>&1', returnStatus: true)
        }
      }
    }
  }
}
