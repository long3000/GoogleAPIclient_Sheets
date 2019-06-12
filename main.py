from pprint import pprint
import auth_flow
import _url_object
import webbrowser

OBJ_GOOGLE_NAME = input("Enter Sheets Name: ")

OBJ_GOOGLE_AUTH = auth_flow.AUTHENTICATE_FLOW()
OBJ_GOOGLE_SHEETS = OBJ_GOOGLE_AUTH.create(OBJ_GOOGLE_NAME)
REPORT_URL = _url_object.default_url + OBJ_GOOGLE_SHEETS.id

print("Report output: %s"%REPORT_URL)

webbrowser.open_new(REPORT_URL)
