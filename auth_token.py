import _token_data
import requests
import gspread
import os
import ast
import json
from oauth2client.service_account import ServiceAccountCredentials #AssertionCredentials
from oauth2client.client import AccessTokenCredentials

def AUTHENTICATE_GOOGLE_DOCS():
    # file_input = file(os.path.join('./client_token.p12'))
    # file_input = open('./client_token.p12','rb')

    # SIGNED_KEY = file_input.read()
    # file_input.close()

    SCOPES = ['https://spreadsheets.google.com/feeds', 'https://docs.google.com/feeds']
    # credentials = ServiceAccountCredentials.('username@gmail.com',SIGNED_KEY,SCOPES)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',SCOPES)
    client = gspread.authorize(credentials)

    # r = requests.post('https://accounts.google.com/o/oauth2/token', data = data)
    
    #credentials.access_token = ast.literal_eval(r.text)['access_token']
    
    # gc = gspread.authorize(AccessTokenCredentials(ast.literal_eval(r.text)['access_token'],'Test'))
    # gc = gspread.authorize(credentials)

    return client

AUTHENTICATE_GOOGLE_DOCS()