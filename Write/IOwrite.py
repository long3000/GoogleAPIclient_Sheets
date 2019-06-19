import gspread
import numpy as numpy
import pandas as pd


def openSheet(client = None, key = None):
    if client == None or key == None:
        print("Client not found")
        pass
    return client.open_by_key(key)

def openWorkSheet(openSheet):
    return openSheet.get_worksheet(0)