import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    './gspread-302412-f233b53a48fc.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('Azure').sheet1

wks.update_acell('A1', 'Hello World!')
print(wks.acell('A1'))
print(wks.acell('A2'))
print(wks.acell('A3').value)
print(wks.cell(1, 1).value)
