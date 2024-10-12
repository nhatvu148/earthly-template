import requests
import json
import os
from dotenv import load_dotenv
from utils import write_json

def refresh_access_token(client_id, client_secret, refresh_token):
    """Refresh the access token using a refresh token."""
    url = "https://oauth2.googleapis.com/token"
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }
    response = requests.post(url, data=payload)
    return response.json()

def read_refresh_token(filename='response.json'):
    """Read refresh token from a JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
        return data.get('refresh_token')

def main():
    load_dotenv()

    client_id = os.getenv('GG_CLIENT_ID')
    client_secret = os.getenv('GG_CLIENT_SECRET')

    refresh_token = read_refresh_token('access_token_response.json')
    print('Refresh Token:', refresh_token)

    refresh_token_response = refresh_access_token(client_id, client_secret, refresh_token)
    print('Refresh Token Response:', refresh_token_response)
    write_json(refresh_token_response, 'refresh_token_response.json')

if __name__ == "__main__":
    main()