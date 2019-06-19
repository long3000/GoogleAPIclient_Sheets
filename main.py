from pprint import pprint
import auth_flow
import _url_object
import webbrowser
import sys, getopt
from Write import IOwrite

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"","ifile=")
    except getopt.GetoptError:
        print ('main.py -i <inputfile>')
        sys.exit(2)
    inputfile = args[0]
    print('Test Data input: ', inputfile)

    OBJ_GOOGLE_NAME = input("Enter Output Sheets Name: ")

    OBJ_GOOGLE_AUTH = auth_flow.AUTHENTICATE_FLOW()
    OBJ_GOOGLE_SHEETS = OBJ_GOOGLE_AUTH.create(OBJ_GOOGLE_NAME)
    REPORT_URL = _url_object.default_url + OBJ_GOOGLE_SHEETS.id

    # Active Sheet
    s = IOwrite.openSheet(client = OBJ_GOOGLE_AUTH, key = OBJ_GOOGLE_SHEETS.id)
    # Active Worksheet
    activeWS = IOwrite.openWorkSheet(s)
    # Write Sample Data
    activeWS.update_cell(1,1,"Test Line")

    print("Report output: %s"%REPORT_URL)
    webbrowser.open_new(REPORT_URL)

if __name__ == '__main__':
    main(sys.argv[1:])
