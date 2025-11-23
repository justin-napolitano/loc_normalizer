# LOC Normalizer

This repository contains the LOC Normalizer project, a tool designed to normalize the Library of Congress (LOC) data schema into a structured database format. The normalized data will then be used to construct a knowledge graph focused on Supreme Court law.

## Features

- Extracts and processes JSON data blobs from GCP storage buckets.
- Normalizes complex JSON structures into flat tables suitable for database ingestion.
- Automates workflows using Google Cloud Run jobs and Docker containers.
- Integrates with Google Cloud services such as Cloud Storage, BigQuery, and Cloud Logging.
- Provides reusable GCP client utilities for storage, logging, and BigQuery operations.

## Tech Stack

- Python (Jupyter Notebooks and scripts)
- Google Cloud Platform (Cloud Storage, BigQuery, Cloud Run, Artifact Registry)
- Docker for containerization
- Bash scripting for automation
- Google Cloud SDK (gcloud CLI)

## Getting Started

### Prerequisites

- Python 3.x
- Docker
- Google Cloud SDK (gcloud) installed and configured
- Access to a GCP project with appropriate permissions

### Installation

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/loc_normalizer.git
cd loc_normalizer
```

2. (Optional) Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Running Locally

- Use the provided Python scripts in `src/` to interact with GCP buckets and process data.
- Ensure your environment is authenticated with GCP credentials (e.g., set `GOOGLE_APPLICATION_CREDENTIALS` or use `gcloud auth application-default login`).

### Building and Deploying the Docker Container

1. Build the Docker image:

```bash
./build.sh
```

2. Deploy the image to Google Cloud Run:

```bash
./deploy.sh
```

These scripts build, tag, push the Docker image to Google Artifact Registry, and deploy it as a Cloud Run service.

## Project Structure

```
loc_normalizer/
├── build.sh                # Script to build Docker image
├── cloudbuild.yaml         # Cloud Build configuration
├── cloudbuildsample.yaml   # Sample Cloud Build config
├── create_deploy_cloud_run_job/  # Possibly deployment-related scripts
├── deploy.sh               # Deployment script for Cloud Run
├── Dockerfile              # Dockerfile for container image
├── dply.sh                 # Additional deployment or utility script
├── execute_job.sh          # Script to execute jobs
├── index.md                # Project overview and plan
├── job_create.sh           # Job creation script
├── post-image.jpeg         # Image used in documentation
├── readme.md               # Secondary readme, possibly outdated
├── requirements.txt        # Python dependencies
├── src/                    # Source code and utilities
│   ├── loc_flattener.py    # JSON normalization logic
│   ├── loc_scraper.py      # Scraper for LOC data
│   ├── gcputils/           # GCP client utilities (storage, logging, BigQuery, secrets)
│   ├── create_last_page_touched_blob.py  # Example GCS interaction
│   └── ...
└── submit.sh               # Script to submit jobs
```

## Future Work / Roadmap

- Complete the normalization workflow to flatten JSON data fully and ingest into BigQuery.
- Expand the scraper to cover more LOC collections and handle pagination robustly.
- Develop the knowledge graph construction using normalized data.
- Improve error handling and logging in scripts.
- Automate CI/CD pipelines using Cloud Build and GitHub Actions.
- Add comprehensive documentation and usage examples.

---

*Note: Some documentation files and scripts indicate ongoing development and may require updates or completion.*