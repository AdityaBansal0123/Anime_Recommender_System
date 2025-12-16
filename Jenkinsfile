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
        stage('DVC Pull'){
            steps{
                withCredentials([file(credentialsId: 'gcp-sa-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh '''
                        set +x  # Hide commands to prevent leaking secrets in logs (optional but good practice)
                        
                        echo "--- Debugging Credentials ---"
                        ls -l $GOOGLE_APPLICATION_CREDENTIALS
                        
                        # Activate Virtual Environment
                        . venv/bin/activate
                        
                        # CRITICAL FIX: Explicitly tell DVC where the key is
                        # Note: Replace 'my-remote' with your actual DVC remote name. 
                        # (Run 'dvc remote list' if you don't know it, usually it is 'storage' or 'origin')
                        
                        # We use --local so it only affects this specific CI run, not the git repo
                        dvc remote modify --local my-dvc-bucket988 credentialpath $GOOGLE_APPLICATION_CREDENTIALS
                        
                        # Now run the pull
                        echo "--- Pulling Data ---"
                        dvc pull
                        
                        # Run your python script
                        python your_script.py
                    '''
                }
            }
        }
    }
}
