import requests
import json
from django.http import Http404
CLIENT_ID = '123'
CLIENT_SECRET = '456'

TOKEN = None


def get_token():
  global TOKEN

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
