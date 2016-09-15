import requests
import json
from django.http import Http404
CLIENT_ID = '123'
CLIENT_SECRET = '456'

TOKEN = None


def get_token():
  global TOKEN
  # In real life, you'd probably use a cache like REDIS to check for tokens first.
  # This is because django-oauth-toolkit does not expire tokens when you ask for new tokens.
  # You could very easily rack up multiple valid tokens for the same user. You don't want to pollute like that

  if not TOKEN:
    response = requests.post(
      'http://127.0.0.1:8000/o/token/',
      data={
          'grant_type': 'password',
          'username': 'test_user1',
          'password': 'test_user1',
          'client_id': CLIENT_ID,
          'client_secret': CLIENT_SECRET
        }
    )
    TOKEN = json.loads(response.text)
    return TOKEN
  else:
    return TOKEN


def refresh_token():
  # When tokens expire (or you just want to get new token),
  # get new tokens by making a POST with your 'refresh_token'
  # to the endpoint: /o/token
  global TOKEN
  token = get_token()
  
  response = requests.post(
    'http://127.0.0.1:8000/o/token/',
    data={
        'grant_type': 'refresh_token',
        'refresh_token': token['refresh_token'],
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
  )
  TOKEN = json.loads(response.text)
  return TOKEN


def revoke_token():
  # Get/Generate a token
  token = get_token()
  # Revoke it with this call
  response = requests.post(
    'http://127.0.0.1:8000/o/revoke_token/',
    data={
      'token': token['access_token']
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET
    }
  )


def get_page():
  try:
    token = get_token()
    print ('Bearer ' + token['access_token'])
    r = requests.get(
      'http://127.0.0.1:8000/list_user',
      headers={
      'Authorization': ('Bearer ' + token['access_token'])
      }
    )
    print r.text
  except:
    raise Http404

get_page()
