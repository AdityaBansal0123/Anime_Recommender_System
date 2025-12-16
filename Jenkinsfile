pipeline{
    agent any
    environment{
        VENV_DIR='venv'
        GCP_PROJECT = 'rare-bastion-464310-r6'
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
        KUBECTL_AUTH_PLUGIN = "/usr/lib/google-cloud-sdk/bin"
    }
    stages{
        // stage("Cloning from Github...."){
        //     steps{
        //         script{
        //             echo 'Cloning from Github....'
        //             checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/AdityaBansal0123/Anime_Recommender_System.git']])
        //         }
        //     }
        // }
        // stage("making a virtual environment"){
        //     steps{
        //         script{
        //             echo 'making a virtual environment'
        //             sh '''
        //             python -m venv ${VENV_DIR}
        //             . ${VENV_DIR}/bin/activate
        //             pip install --upgrade pip 
        //             pip install -e .
        //             pip install dvc
        //             '''
        //         }
        //     }
        // }
        stage('DVC Pull'){
            steps{
<<<<<<< HEAD
                withCredentials([file(credentialsId: 'gcp-sa-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
=======
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
>>>>>>> 253f7d66f526700d1ca3b7158b5219abe7e538c5
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
<<<<<<< HEAD
=======
                }
            }
        }
        stage('Build and Push Image to GCR'){
            steps{
                withCredentials([file(credentialsId:'gcp-key' , variable: 'GOOGLE_APPLICATION_CREDENTIALS' )]){
                    script{
                        echo 'Build and Push Image to GCR'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud auth configure-docker --quiet
                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .
                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
            }
        }
         stage('Deploying to Kubernetes'){
            steps{
                withCredentials([file(credentialsId:'gcp-key' , variable: 'GOOGLE_APPLICATION_CREDENTIALS' )]){
                    script{
                        echo 'Deploying to Kubernetes'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}:${KUBECTL_AUTH_PLUGIN}
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                        gcloud config set project ${GCP_PROJECT}
                        gcloud container clusters get-credentials ml-app-cluster --region us-central1
                        kubectl apply -f deployment.yaml
                        '''
                    }
>>>>>>> 253f7d66f526700d1ca3b7158b5219abe7e538c5
                }
            }
        }
    }
}
