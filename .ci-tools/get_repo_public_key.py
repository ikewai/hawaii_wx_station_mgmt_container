# gets the public key of a given repo.
# inputs: repo org and name, auth token with read access

import requests

def get_repo_public_key(org: str, repo: str, access_token: str) -> str:
    base_url = "https://api.github.com"
    endpoint = "actions/secrets/public-key"
    url = f"base_url/{org}/{repo}/{endpoint}"

    headers = {
    # accept: application/vnd.github.v3+json
    # authorization method: token bearer
    # token: get from environment variable
    }

    res = requests.get(url=url, headers=headers)