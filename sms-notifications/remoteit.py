import requests
import json
import os


def get_auth_token() -> str:
    """
    Get the session auth token from the remote.it API. This is needed to
    authenticate all further requests to the remote.it API.

    Returns:
        str: The authentication token.
    """

    headers = {
        "developerkey": os.environ["REMOTEIT_DEVELOPER_KEY"]
    }

    body = {
        "password": os.environ["REMOTEIT_PASSWORD"],
        "username": os.environ["REMOTEIT_USERNAME"]
    }

    url = "https://api.remot3.it/apv/v27/user/login"

    response = requests.post(url, data=json.dumps(body), headers=headers)
    response_body = response.json()
    return response_body["token"]


def get_ssh_url() -> str:

    pass
