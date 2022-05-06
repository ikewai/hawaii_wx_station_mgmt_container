#!/bin/python3
import requests

def get_new_tokens(ike_url, ike_key, ike_secret, ike_refresh) -> dict:

    params = {
        "grant_type": "refresh_token",
        "refresh_token": ike_refresh,
        "client_id": ike_key,
        "client_secret": ike_secret,
    }

    r = requests.post(url=ike_url, params=params)
    # TODO make sure request is happy
    new_access_token = r.json()['access_token']
    new_refresh_token = r.json()['refresh_token']
    return {
        "access": new_access_token, 
        "refresh": new_refresh_token
    }