#!/bin/bash

# Set variables
IMAGE_NAME="loc-flattener-image"
PROJECT_ID="strategic-kite-431518-d87"
REGION="us-west2"
ARTIFACT_REGISTRY="us-west2-docker.pkg.dev/$PROJECT_ID/$IMAGE_NAME"

# Build the Docker image locally
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Tag the Docker image
echo "Tagging Docker image..."
docker tag $IMAGE_NAME $ARTIFACT_REGISTRY

# Authenticate Docker to Google Artifact Registry
echo "Authenticating Docker with Google Artifact Registry..."
gcloud auth configure-docker $REGION-docker.pkg.dev

# Push the Docker image to Google Artifact Registry
echo "Pushing Docker image to Google Artifact Registry..."
docker push $ARTIFACT_REGISTRY

# Deploy to Google Cloud Run (optional)
echo "Deploying to Google Cloud Run..."
gcloud run deploy loc-flattener-service \
  --image $ARTIFACT_REGISTRY \
  --region $REGION

echo "Deployment complete."
