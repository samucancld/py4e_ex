import requests
from bearer_authenticator import bearer_oauth
def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()