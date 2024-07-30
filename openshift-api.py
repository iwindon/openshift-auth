import requests
import os

def get_token():
    """Function to retrieve the token froim the OpenShift Cluster"""
    cluster_url = "https://oauth-openshift.apps.openshift.example.com"
    username = os.environ["USER_NAME"]
    password = os.environ["PASSWORD"]
    cert_path = os.path.join(os.path.dirname(__file__), "cert.pem")

    response = requests.get(f"{cluster_url}/oauth/authorize?client_id=openshift-challenging-client&response_type=token",
                           auth=(username, password), timeout=15, verify=cert_path, allow_redirects=True)
    token = response.url.split("access_token=")[1].split("&")[0]
    return token

token = get_token()