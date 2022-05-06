#!/bin/python3
from get_new_tokens import get_new_tokens
from encrypt_token import encrypt_token
from update_secret_rest_call import put_secret
from get_repo_public_key import get_repo_public_key
import os

tokens: dict = get_new_tokens(
    ike_url=os.environ['ike_url'],
    ike_key=os.environ['ike_key'],
    ike_secret=os.environ['ike_secret'],
    ike_refresh=os.environ['ike_refresh'],
    gh_repo_read=os.environ['gh_repo_read']
)

# Get the repo's public key, this will be used to encrypt the secrets.
pubkey = get_repo_public_key(
    org="ikewai", 
    repo="hawaii_wx_station_mgmt_container", 
    access_token=tokens['gh_repo_read']
    )


# to be continued...