'''Run with PyTest'''

import requests
import pytest

local_endpoint = "http://127.0.0.1:5000/"
base_endpoint = local_endpoint + 'basic'
secure_endpoint = local_endpoint + 'secure'

def process_response(response):
    r_text = response.text
    try:
        response.raise_for_status()
        return r_text
    except:
        raise BaseException(r_text)

def test_base_get_request():
    r = requests.get(base_endpoint)
    return process_response(r)

def test_base_post_request():
    data = dict(key='value')
    r = requests.post(base_endpoint, json=data)
    return process_response(r)

def test_secure_get_request():
    r = requests.get(secure_endpoint, headers=dict(Authorization='Some Token'))
    return process_response(r)

def test_secure_post_request():
    data = dict(key='value')
    r = requests.post(secure_endpoint, json=data, headers=dict(Authorization='Some Token'))
    return process_response(r)

# verify that a get request w/o an auth header to a secure endpoint is rejected
def test_secure_get_request_without_auth():
    r = requests.get(secure_endpoint)
    with pytest.raises(BaseException):
        process_response(r)

# verify that a post request w/o an auth head
def test_secure_post_request_without_auth():
    data = dict(key='value')
    r = requests.post(secure_endpoint, json=data)
    with pytest.raises(BaseException):
        process_response(r)