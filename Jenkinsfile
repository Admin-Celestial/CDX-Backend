node {
    try {
        stage('Checkout') {
            checkout scm
            
            // Log last changes
            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')
            slackSend color: "warning", message: "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"
        }

        stage('Test') {
            // Define AWS credentials
            withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-credentials', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                // Activate virtual environment
                sh 'virtualenv env -p python3.10'
                sh '. env/bin/activate'
                
                // Install dependencies and run tests
                sh 'env/bin/pip install -r requirements.txt'
            }
        }

        stage('Deploy') {
            // Print SSH private key for debugging
            sh 'cat ~/.ssh/id_rsa'

            // Fetch the deployment script from GitHub
            sh 'wget https://raw.githubusercontent.com/vivek-celtech/CDX-Backend/main/deployment/deploy_prod.sh -O deploy_prod.sh'

            // Grant execute permissions to the deployment script
            sh 'chmod +x deploy_prod.sh'
            
            // Execute the deployment script
            sh './deploy_prod.sh'
        }

        stage('Publish results') {
            slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
        }
    } catch (err) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
        throw err
    }
}
