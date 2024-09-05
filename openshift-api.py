import requests
import os

def get_token(cluster, env, core):
    """Function to retrieve the token froim the OpenShift Cluster"""
    if core is True:
        domain = "core.openshift.example.com"
    else:
        domain = "openshift.example.com"
    cluster_url = f"https://oauth-openshift.apps.{cluster}-{env}.{domain}"
    username = os.environ["USER_NAME"]
    password = os.environ["PASSWORD"]
    cert_path = os.path.join(os.path.dirname(__file__), "cert.pem")

    response = requests.get(f"{cluster_url}/oauth/authorize?client_id=openshift-challenging-client&response_type=token",
                           auth=(username, password),
                           timeout=15,
                           verify=cert_path,
                           allow_redirects=True
                    )
    token = response.url.split("access_token=")[1].split("&")[0]
    return token

openshift_token = get_token("dallas", "dev", False)