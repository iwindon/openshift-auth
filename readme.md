# OpenShift API Token Retrieval

This Python script retrieves an OAuth token from an OpenShift Cluster using the `requests` library. The script is designed to handle SSL verification using a self-signed certificate.

## Prerequisites

- Python 3.x
- `requests` library
- A self-signed certificate file (`cert.pem`) located in the same directory as the script
- Environment variables `USER_NAME` and `PASSWORD` set with your OpenShift credentials

## Environment Variables

Ensure that the following environment variables are set before running the script:

- `USER_NAME`: Your OpenShift username
- `PASSWORD`: Your OpenShift password

## How It Works

1. The script imports the necessary libraries: `requests` and `os`.
2. It defines a function `get_token()` that:
   - Constructs the OpenShift OAuth URL.
   - Retrieves the username and password from environment variables.
   - Constructs the path to the self-signed certificate file (`cert.pem`).
   - Makes a GET request to the OpenShift OAuth endpoint with the provided credentials and certificate.
   - Extracts the OAuth token from the response URL.
3. The script calls the `get_token()` function and stores the token in the `token` variable.

## Usage

1. Ensure you have the `requests` library installed. You can install it using pip:
   ```sh
   pip install requests

2. Set the required environment variables:
    ```sh
    export USER_NAME=your_username
    export PASSWORD=your_password

3. Place your self-signed certificate file (cert.pem) in the same directory as the script.
4. Run the script:
    ```sh
    python openshift-api.py

## Parameters

* `cluster` (str): The name of the OpenShift cluster.
* `env` (str): The environment (e.g., `dev`, `prod`).
* `core` (bool): A flag to determine the domain to use.

Returns
* `str`: The OAuth token.~~

## Example
```sh
import requests
import os

def get_token():
    """Function to retrieve the token from the OpenShift Cluster"""
    cluster_url = "https://oauth-openshift.apps.openshift.example.com"
    username = os.environ["USER_NAME"]
    password = os.environ["PASSWORD"]
    cert_path = os.path.join(os.path.dirname(__file__), "cert.pem")

    response = requests.get(f"{cluster_url}/oauth/authorize?client_id=openshift-challenging-client&response_type=token",
                           auth=(username, password), timeout=15, verify=cert_path, allow_redirects=True)
    token = response.url.split("access_token=")[1].split("&")[0]
    return token

token = get_token()
print(token)
```
## Notes
*   Ensure that the `cert.pem` file is correctly placed and accessible.
*   Handle the OAuth token securely and avoid exposing it in logs or output.

## License
This project is licensed under the MIT License.