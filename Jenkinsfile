pipeline{
    agent any
    environment{
        VENV_DIR='venv'
    }
    stages{
        stage("Cloning from Github...."){
            steps{
                script{
                    echo 'Cloning from Github....'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/AdityaBansal0123/Anime_Recommender_System.git']])
                }
            }
        }
        stage("making a virtual environment"){
            steps{
                script{
                    echo 'making a virtual environment'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip 
                    pip install -e .
                    pip install dvc
                    '''
                }
            }
        }
        stage('DVC Pull') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GCP_SA_KEY')]) {
                    script {
                        echo 'Configuring DVC remote and pulling...'
                        sh '''
                        # Activate Virtual Env
                        . ${VENV_DIR}/bin/activate
                        
                        # Set Credentials
                        export GOOGLE_APPLICATION_CREDENTIALS=$GCP_SA_KEY
                        
                        # --- THE FIX ---
                        # Explicitly tell DVC where the bucket is.
                        # -d sets it as default.
                        # -f overwrites any existing broken config.
                        dvc remote add -d -f storage gs://my-dvc-bucket988
                        
                        # Now pull
                        dvc pull
                        '''
                    }
                }
            }
        }
    }
}
