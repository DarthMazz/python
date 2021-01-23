import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

from bs4 import BeautifulSoup
import urllib.error
import urllib.request

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

key_file_name = './gspread-302412-f233b53a48fc.json'


def get_credentials():
    return sac.from_json_keyfile_name(key_file_name, scope)


def get_worksheet(credentials, worksheet_name):
    gc = gspread.authorize(credentials)
    return gc.open(worksheet_name).sheet1


def get_rows(worksheet):
    rows = list()
    # worksheet.update_acell('A1', 'Hello World!')
    # rows.append(worksheet.acell('A1'))
    # rows.append(worksheet.acell('A2'))
    # rows.append(worksheet.acell('A3').value)
    # rows.append(worksheet.cell(1, 1).value)
    row = 1
    row_value = 'start'
    while len(row_value) > 0:
        row_value = worksheet.cell(1, row).value
        if len(row_value) > 0:
            rows.append(row_value)
        row += 1
    
    return rows


def analyze_url(urls):
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
        'AppleWebKit/537.36 (KHTML, like Gecko) '\
        'Chrome/55.0.2883.95 Safari/537.36 '

    find_urls = list()
    for url in urls:
        req = urllib.request.Request(url, headers={'User-Agent': ua})
        html = urllib.request.urlopen(req)
        soup = BeautifulSoup(html, "html.parser")
        url_list = [img.div.img['src'] for img in soup.select('.newsFeed_item_thumbnail')]
        find_urls.extend(url_list)

    return find_urls


def print_rows(rows):
    for row in rows:
        print(row)


def main():
    credentials = get_credentials()
    worksheet = get_worksheet(credentials, 'Azure')
    rows = get_rows(worksheet)
    urls = analyze_url(rows)
    print_rows(urls)


if __name__ == '__main__':
    main()
