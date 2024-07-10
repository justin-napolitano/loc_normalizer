+++
title =  "GCP Cloud Run: LOC Normalizer"
date = "2024-04-28"
description = "Normalizing a JSON into A DB.. Autonomously. "
author = "Justin Napolitano"
tags = ['git', 'python', 'gcp', 'bash','workflow automation', 'docker','containerization']
images = ["images/feature-gcp.png"]
categories = ["projects"]
+++


# Library of Congress Normalizer Job

This [repo](https://github.com/justin-napolitano/loc_normalizer) normalizes the existing library of congress schema into a db that wil then be used to construct a knowledge graph of supreme court law. 

## Plan

1. Setup a venv to run locally
2. Install requirements
3. Write out the script to interface with gcp
4. Set up a docker container and test locally
5. build the image
6. upload to gcp
7. create the job

## Setup the venv

### Install
I installed virtualenv locally on ubuntu

### Create
I then run ```virtualenv {path to venvs}```

### Activate

Then source the venv bin to activate

```source {path to venv}/bin/activate```
   
### Install requirements

``` pip install -r requirements.txt```

## Write out the Script

### Steps

1. Access the loc_scraper Bucket
2. Grab a json blob
3. Process the blob
4. Move the blob to a processed bucket


### Data Organization

I want to create workflow class with the following methods

1. get_creds
2. grab_blob
3. process_blob
4. move_blob

The process_blob method will be a lot of work.  I might just flatten the json and dump into a table. I will then write a normalization workflow


### Get Creds

If running locally I will need some creds in the enviornment.  I'll just create a .env file and import at runtime if running locally. 





## Setup the Docker Container

### The Dockerfile

Also available on [github](https://github.com/justin-napolitano/loc_normalizer/blob/main/Dockerfile)


```
# # Use the Alpine Linux base image
# FROM alpine:latest

# # Set the working directory inside the container
# WORKDIR /app

# # Copy a simple script that prints "Hello, World!" into the container
# COPY /src/hello.sh .

# # Make the script executable
# RUN chmod +x hello.sh

# # Define the command to run when the container starts
# CMD ["./hello.sh"]


# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app
COPY requirements.txt /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container launches
CMD ["python", "loc_scraper.py"]
```


## Quickstart


### Gcloud cli
After this you will have to install gcloud cli and configure you're local environment. I will write up some scripts in a subsequent post to automate this process... but for the time being check out this ["link"](https://cloud.google.com/sdk/docs/install)

### Create the image

In the repo there is a a bash script called ```build.sh``` that will need to be updated to according to your gcp project.

```bash
gcloud builds submit --region=us-west2 --config cloudbuild.yaml
```

It calls ```cloudbuild.yaml``` which might need to be updated for you, but the following the should work.

```yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  script: |
    docker build -t us-west2-docker.pkg.dev/$PROJECT_ID/supreme-court-scraper/supreme-court-scraper-image:dev .
  automapSubstitutions: true
images:
- 'us-west2-docker.pkg.dev/$PROJECT_ID/supreme-court-scraper/supreme-court-scraper-image:dev'
```

### Following creation of the imge 
Next you can create a job on gcp by runnning the ```job_create.sh``` script... or by copying the code below and chaging yourproject to the correct project-name

```bash
gcloud run jobs create supreme-court-scraper --image us-west2-docker.pkg.dev/yourproject/supreme-court-scraper/supreme-court-scraper-image:dev \
```

### Executing the job

Once complete you can execute the job by running the ```execute_job.sh``` script or by running 

```bash
gcloud run jobs execute supreme-court-scraper
```

### Putting it all together

In a perfect world the following should work. Note that src/.env should be set with your environmental variables such as ```$GCPPROJECTID``` 

```bash
source src/.env \
&& ./build.sh \ 
&& ./job_create.sh \
&& ./execute_job.sh
```

## Running locally

The python script in the ```/src``` can be run locally, however it should be modified if you choose not to use gcp.  There are a number of functions within that can easily be modified to permit writing to the local directory. 


## Documentation Sources
1. ["Google Cloud Run Jobs Automation"](https://cloud.google.com/run/docs/create-jobs)
