# Docker Images on GCP quickstart

Source : ```https://cloud.google.com/build/docs/build-push-docker-image```



## Create the hello world bash script

```bash
touch quickstart.sh && echo "echo 'Hello World! The time is $(date).'" > quickstart.sh && chmod +x quickstart.sh
```

### Create the Docker File

```bash
touch Dockerfile &&
echo  \
"FROM alpine \n
COPY quickstart.sh \n
CMD ["/quickstart.sh"]
" > Dockerfile
```

## Create the Docker Artifact Repo on GCP
Run this

```bash
gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker --location=us-east1 --description="Docker repository"
```