import os
import requests
from data_and_connections.setup import requests_object

lens_url = os.environ['LENS_POST_URL']
lens_token = os.environ['LENS_JUAN_TOKEN']

def ping_test():
    return