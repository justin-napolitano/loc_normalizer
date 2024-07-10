# loc_flattener.py
# library_of_congress_scraper.py

from __future__ import print_function
from gcputils.gcpclient import GCSClient
from gcputils.GoogleCloudLogging import GoogleCloudLogging
from bs4 import BeautifulSoup
import requests
import json
import os
import time
from pprint import pprint
import html
from flatten_json import flatten
import google.cloud.logging
import logging
import argparse

def initialize_gcs_client(project_id, credentials_path=None):
    return GCSClient(project_id, credentials_path=credentials_path)
    

def initialize_google_cloud_logging_client(project_id, credentials_path=None):
    return GoogleCloudLogging(project_id, credentials_path=credentials_path)

def list_gcs_buckets(client):
    try:
        buckets = client.list_buckets()
        print("Buckets:", buckets)
        logging.info(f"Buckets: {buckets}")
    except Exception as e:
        logging.error(f"Error listing buckets: {e}")

def create_gcs_bucket(client, bucket_name):
    try:
        bucket = client.create_bucket(bucket_name=bucket_name)
        logging.info(bucket)
        print(bucket)
    except Exception as e:
        logging.error(f"Error creating bucket: {e}")

def main():
    parser = argparse.ArgumentParser(description='Run the script locally or in the cloud.')
    parser.add_argument('--local', action='store_true', help='Run the script locally with credentials path')
    args = parser.parse_args()

    project_id = os.getenv('GCP_PROJECT_ID', 'smart-axis-421517')
    bucket_name = os.getenv('BUCKET_NAME', 'loc-scraper')

    credentials_path = None
    if args.local:
        credentials_path = os.getenv('GCP_CREDENTIALS_PATH', 'secret.json')

    # Initialize logging
    logging_client = initialize_google_cloud_logging_client(project_id,credentials_path)
    logging_client.setup_logging()

    # Initialize the Google Cloud Client
    gcs_client = initialize_gcs_client(project_id, credentials_path)
    
    #List Buckets for testing
    list_gcs_buckets(gcs_client)

    # Pop a blob to test ability to access within a bucket

    # Grab A blob from the heap
    first_blob = gcs_client.pop_blob(bucket_name)
    if first_blob:
        print(f"First blob name: {first_blob.name}")

    # create_gcs_bucket(gcs_client, bucket_name)

if __name__ == "__main__":
    main()
