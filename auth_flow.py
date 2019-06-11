from oauth2client.client import OAuth2WebServerFlow
from oauth2client import tools
from oauth2client.file import Storage
from auth_cred import CLIENT_ID as ci
from auth_cred import CLIENT_SECRET as cs
import gspread
import webbrowser

SCOPES = 'https://spreadsheets.google.com/feeds https://docs.google.com/feeds',

def AUTHENTICATE_FLOW():
    flow = OAuth2WebServerFlow(
        client_id = ci,
        client_secret = cs,
        scope = SCOPES,
        redirect_uri = 'http://example.com/auth_return'
    )

    storage = Storage("client_secret.json")
    credentials = tools.run_flow(flow,storage)

    gc = gspread.authorize(credentials)
    # print("Access Token: %s"%credentials.access_token)

    return gc