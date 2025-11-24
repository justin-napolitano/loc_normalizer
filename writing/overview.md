---
slug: github-loc-normalizer-writing-overview
id: github-loc-normalizer-writing-overview
title: 'LOC Normalizer: Transforming LOC Data for Knowledge Graphs'
repo: justin-napolitano/loc_normalizer
githubUrl: https://github.com/justin-napolitano/loc_normalizer
generatedAt: '2025-11-24T17:38:20.245Z'
source: github-auto
summary: >-
  I built the LOC Normalizer to simplify the process of transforming Library of
  Congress (LOC) data into a structured format. The ultimate goal is to use this
  normalized data to power a knowledge graph focused on Supreme Court law. It's
  a pretty niche tool, but I think it fills an important gap.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

I built the LOC Normalizer to simplify the process of transforming Library of Congress (LOC) data into a structured format. The ultimate goal is to use this normalized data to power a knowledge graph focused on Supreme Court law. It's a pretty niche tool, but I think it fills an important gap.

## Why LOC Normalizer Exists

The LOC has an immense wealth of information, but working with its complex JSON data can be a pain. When I started digging into LOC data for personal research, I realized there wasn't an efficient way to process and normalize this data for database use. So, I created the LOC Normalizer. It takes messy JSON blobs and transforms them into tidy tables that you can readily ingest into databases.

## Key Design Decisions

I wanted this project to be robust yet user-friendly. Here are some key design choices I made:

- **Automation**: I leveraged Google Cloud Run for seamless automation. It allows for serverless execution of jobs, which means less hassle with infrastructure.
- **Modularity**: The code is structured with reusable components. Whether you're dealing with storage, logging, or BigQuery, I've built utility scripts that make life easy.
- **Simplicity**: The design focuses on clear functionality without unnecessary complexity. If you need to get data from the LOC and process it, that’s the main goal.

## Tech Stack and Tools

My tech stack mainly revolves around Python and Google Cloud services. Here's a quick rundown:

- **Python**: I used it for both Jupyter Notebooks and scripts. It's flexible and great for data manipulation.
- **Google Cloud Platform**:
  - **Cloud Storage**: For storing the raw LOC JSON data.
  - **BigQuery**: For querying the normalized data.
  - **Cloud Run**: For running jobs in the cloud without worrying about servers.
  - **Artifact Registry**: To manage Docker images.
- **Docker**: Containerized the workflow to ensure consistency across environments.
- **Bash**: Used for scripting automation tasks.

## Features that Stand Out

The LOC Normalizer has quite a few features I’m proud of:

- **Data Extraction**: Pulls JSON data from Google Cloud Storage.
- **Normalization**: Flattens complex JSON structures into tables.
- **Automated Workflow**: All operations run smoothly in Google Cloud, thanks to Cloud Run.
- **Client Utilities**: Includes reusable GCP client utilities for seamless operations across GCP services.

## Installation and Getting Started

If you want to try the LOC Normalizer, it’s pretty simple to set up. Here’s a quick guide:

1. Clone the repository:
   ```bash
   git clone https://github.com/justin-napolitano/loc_normalizer.git
   cd loc_normalizer
   ```

2. Set up a Python environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

To run it locally, you'll need to authenticate with your GCP credentials. Just set the `GOOGLE_APPLICATION_CREDENTIALS` or log in via `gcloud`.

## Project Structure

Here’s a snapshot of how the codebase is structured:

```
loc_normalizer/
├── build.sh                # Build Docker image
├── deploy.sh               # Deployment script for Cloud Run
├── src/                    # Source code
│   ├── loc_flattener.py    # Logic to normalize JSON
│   ├── loc_scraper.py      # Data scraper for LOC
│   ├── gcputils/           # Utilities for GCP operations
└── ...
```

The directory structure is designed to be intuitive. You should find everything you need in the `src/` folder.

## Trade-offs

No project is without its compromises. Here are a few challenges I faced:

- **Performance**: While cloud solutions are powerful, they can come with latency. I'll need to monitor performance and optimize where necessary.
- **Documentation**: I'm constantly improving the documentation. Some parts still need updates as I refine features.
- **Complexity of JSON**: The complexity of LOC data can lead to edge cases in normalization. Error handling needs more robustness.

## What’s Next on My To-Do List

There’s always room for improvement. Here’s what I’m focusing on next:

- **Complete Normalization**: I aim to finish the workflow for flattening the JSON data for BigQuery ingestion.
- **Expand Data Coverage**: I'll enhance the scraper to fetch more data collections from the LOC.
- **Knowledge Graph**: Developing the graph itself using the normalized data is a big goal on my radar.
- **Automation and CI/CD**: Implementing CI/CD pipelines using Cloud Build and GitHub Actions is essential for maintaining continuous integration.

## Stay Updated

If you find this project interesting or want to see how it evolves, I share updates on Mastodon, Bluesky, and Twitter/X. Follow along if you want to keep in the loop!

The LOC Normalizer is a project born from necessity. I'm excited to see where it goes and hope it makes working with LOC data a bit easier for anyone who might need it.
