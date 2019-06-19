from pprint import pprint
import auth_flow
import _url_object
import webbrowser
import sys
from Write import IOwrite

OBJ_GOOGLE_NAME = input("Enter Sheets Name: ")

OBJ_GOOGLE_AUTH = auth_flow.AUTHENTICATE_FLOW()
OBJ_GOOGLE_SHEETS = OBJ_GOOGLE_AUTH.create(OBJ_GOOGLE_NAME)
REPORT_URL = _url_object.default_url + OBJ_GOOGLE_SHEETS.id

# Active Sheet
s = IOwrite.openSheet(client = OBJ_GOOGLE_AUTH, key = OBJ_GOOGLE_SHEETS.id)
# Active Worksheet
activeWS = IOwrite.openWorkSheet(s)
# Write Sample Data
activeWS.update_cell(1,1,"Test Line")

if __name__ == '__main__':
    print("Report output: %s"%REPORT_URL)
    webbrowser.open_new(REPORT_URL)

