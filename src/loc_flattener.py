#loc_flattener.py 
#library_of_congress_scraper.py
from __future__ import print_function
from gcputils.gcpclient import GCSClient
from bs4 import BeautifulSoup
import requests
# import lxml.etree as etree
# import xml.etree.ElementTree as ET
import json
# import pandas as pd
import os
import time
# import random
# import math
from pprint import pprint
#import load_vars as lv
import html
# import yaml
# from yaml import Loader, Dumper
# import glob
# import datetimeResult
import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google.oauth2 import service_account
# from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from flatten_json import flatten
# import networkx as nx
# import matplotlib
# from networkx.readwrite import json_graph
# import matplotlib.pyplot as plt
# import tracemalloc
# import os
#from ratelimiter import RateLimiter

# Imports the Cloud Logging client library
import google.cloud.logging
import logging


def main():
    #hardcoding this.. idk if it is better to add it to the config or not. 
    # i have thoughts on both. 
    # just hardcoding to limit th enumber of htings to be aware of when working with this script
    project_id = 'smart-axis-421517'
    # last_page_num = read_last_page_num() + 1
    # print(f"Starting at {last_page_num}")

    gcs_client = GCSClient(project_id, credentials_path=None)
    
    # Instantiates a cloud loggingclient
    logging_client = google.cloud.logging.Client()

    # Retrieves a Cloud Logging handler based on the environment
    # you're running in and integrates the handler with the
    # Python logging module. By default this captures all logs
    # at INFO level and higher
    logging_client.setup_logging()

    # List buckets to test client authorization
    buckets = gcs_client.list_buckets()
    print("Buckets:", buckets)
    logging.info(f"Buckets: {buckets}")

    # creating a new bucket if it doesn't exist
    bucket_name = "loc-scraper"

    # bucket = gcs_client.create_bucket(bucket_name=bucket_name)
    # logging.info(bucket)
    # print(bucket)