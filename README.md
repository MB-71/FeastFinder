## Commands to Build and Run
1. Navigate to google cloud and login:
    - https://console.cloud.google.com/

2. Open Cloud Terminal

3. Git Clone Repo:
    ```
        git clone https://gitlab.com/brewer7/cloud-brewer-brewer7.git
    ```
    or ssh:
    ```
        git clone git@gitlab.com:brewer7/cloud-brewer-brewer7.git
    ```

4. Login to GitLab

5. Change into project directory:
    ```
        cd cloud-brewer-brewer7/final/
    ```

6. Docker Commands:
    - Build: 
    ```
        docker build -f Dockerfile -t final .
    ```
    - Tag: 
    ```
        docker tag final:latest gcr.io/${GOOGLE_CLOUD_PROJECT}/final
    ```
    - Push:
    ```
        docker push gcr.io/${GOOGLE_CLOUD_PROJECT}/final
    ```
    - Submit to Google Cloud Build:
    ```
        gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/final
    ```

7. Create IAM service account and add policy:
    - 
    ```
        gcloud iam service-accounts create finalfeast
    ```
    - Add IAM policy bindings
    ```
        gcloud projects add-iam-policy-binding cloud-brewer7 \
            --member="serviceAccount:finalfeast@cloud-brewer7.iam.gserviceaccount.com" \
            --role="roles/run.invoker"
        gcloud projects add-iam-policy-binding cloud-brewer7 \
            --member="serviceAccount:finalfeast@cloud-brewer7.iam.gserviceaccount.com" \
            --role="roles/storage.admin"
     ```

8. To deploy run: 
    ```
        gcloud run deploy feastfinder --image gcr.io/${GOOGLE_CLOUD_PROJECT}/final \
            --service-account finalfeast@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com \
            --region us-west1 --allow-unauthenticated
    ```

## Clean Up
1. Remove the service: 
    ```
        gcloud run services delete feastfinder --region us-west1
    ```
    
2. Remove the container image:
    ```
        gcloud container images delete gcr.io/${GOOGLE_CLOUD_PROJECT}/final
        docker rmi -f $(docker images -q)
    ```

3. Remove Service Account:
    ```
        gcloud iam service-accounts delete finalfeast@cloud-brewer7.iam.gserviceaccount.com
    ```
