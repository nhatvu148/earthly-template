import requests
import os
from dotenv import load_dotenv
from utils import write_json

def get_access_token(client_id, client_secret, authorization_code):
    """Exchange authorization code for access token."""
    url = "https://oauth2.googleapis.com/token"
    payload = {
        'code': authorization_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': 'http://localhost:3001',
        'grant_type': 'authorization_code'
    }
    response = requests.post(url, data=payload)
    return response.json()

def main():
    load_dotenv()

    client_id = os.getenv('GG_CLIENT_ID')
    client_secret = os.getenv('GG_CLIENT_SECRET')
    authorization_code = os.getenv('GG_AUTH_CODE')

    access_token_response = get_access_token(client_id, client_secret, authorization_code)
    print('Access Token Response:', access_token_response)
    write_json(access_token_response, 'access_token_response.json')

if __name__ == "__main__":
    main()