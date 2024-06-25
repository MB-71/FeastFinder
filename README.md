## Commands to Build and Run
1. Navigate to google cloud and login:
    - https://console.cloud.google.com/

2. Open Cloud Terminal

3. Git Clone Repo:
    ```
        git clone https://github.com/MB-71/FeastFinder.git
    ```
    or ssh:
    ```
        git clone git@github.com:MB-71/FeastFinder.git
    ```

4. Login to ~~GitLab~~ GitHub

5. Change into project directory:

    ~~`
        cd cloud-brewer-brewer7/final/
    `~~

    ```
        cd FeastFinder/
    ```

6. Docker Commands:
    - Build: 
    ```
        docker build -f Dockerfile -t feastfinder .
    ```
    - Tag: 
    ```
        docker tag feastfinder:latest gcr.io/${GOOGLE_CLOUD_PROJECT}/feastfinder
    ```
    - Push:
    ```
        docker push gcr.io/${GOOGLE_CLOUD_PROJECT}/feastfinder
    ```
    - Submit to Google Cloud Build:
    ```
        gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/feastfinder
    ```

7. Create IAM service account and add policy:
    ```
        gcloud iam service-accounts create feastfinder
    ```
    - Add IAM policy bindings
    ```
        gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
            --member="serviceAccount:feastfinder@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
            --role="roles/run.invoker"
        gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
            --member="serviceAccount:feastfinder@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
            --role="roles/storage.admin"
     ```

8. To deploy run: 
    ```
        gcloud run deploy feastfinder --image gcr.io/${GOOGLE_CLOUD_PROJECT}/feastfinder \
            --service-account feastfinder@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com \
            --region us-west1 --allow-unauthenticated
    ```

## Clean Up
1. Remove the service: 
    ```
        gcloud run services delete feastfinder --region us-west1
    ```
    
2. Remove the container image:
    ```
        gcloud container images delete gcr.io/${GOOGLE_CLOUD_PROJECT}/feastfinder
        docker rmi -f $(docker images -q)
    ```

3. Remove Service Account:
    ```
        gcloud iam service-accounts delete feastfinder@cloud-brewer7.iam.gserviceaccount.com
    ```
