import requests

def get_user(user_id, base_url):
    return requests.get(f"{base_url}/users/{user_id}")
