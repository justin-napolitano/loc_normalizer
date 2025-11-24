---
slug: github-loc-normalizer-note-technical-overview
id: github-loc-normalizer-note-technical-overview
title: LOC Normalizer
repo: justin-napolitano/loc_normalizer
githubUrl: https://github.com/justin-napolitano/loc_normalizer
generatedAt: '2025-11-24T18:40:42.465Z'
source: github-auto
summary: >-
  The LOC Normalizer is a tool that transforms the Library of Congress (LOC)
  data schema into a structured database format. This normalized data helps
  build a knowledge graph focused on Supreme Court law.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

The LOC Normalizer is a tool that transforms the Library of Congress (LOC) data schema into a structured database format. This normalized data helps build a knowledge graph focused on Supreme Court law.

### Key Components
- **Python**: For scripts and Jupyter Notebooks.
- **Google Cloud Platform**: Uses services like Cloud Storage and BigQuery.
- **Docker**: Containerizes the application for deployment.
- **Bash scripting**: Automates tasks.

### Quick Start
1. Clone the repo:
    ```bash
    git clone https://github.com/justin-napolitano/loc_normalizer.git
    cd loc_normalizer
    ```
2. (Optional) Set up a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

**Gotcha**: Ensure you authenticate your environment with GCP before running scripts. Use `gcloud auth application-default login` or set `GOOGLE_APPLICATION_CREDENTIALS`.
