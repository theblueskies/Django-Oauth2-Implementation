import requests
import json
from django.http import Http404
CLIENT_ID = '123'
CLIENT_SECRET = '456'

def get_token():
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
  return response.text

def get_page():
  try:
    token = json.loads(get_token())
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