import _token_data
import requests
import gspread
import os
import ast
import json
from oauth2client.service_account import ServiceAccountCredentials #AssertionCredentials
from oauth2client.client import AccessTokenCredentials

def AUTHENTICATE_GOOGLE_DOCS():
    SCOPES = ['https://spreadsheets.google.com/feeds', 'https://docs.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',SCOPES)
    client = gspread.authorize(credentials)
    return client

# AUTHENTICATE_GOOGLE_DOCS()