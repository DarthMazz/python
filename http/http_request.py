import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class HttpRequest:
    def __init__(self, url):
        self.url = url

    def __del__(self) -> None:
        pass

    def request(self):
        s = requests.Session()
        # backoff_factor = 3
        # for retry_count in range(1, 6):
        #     print(f'backoff_factor : {backoff_factor}, retry_count : {retry_count}, retry_time: {backoff_factor * (2 ** (retry_count - 1))}')
        retries = Retry(total=3, #リトライ回数
                        backoff_factor=1, #リトライ間隔(backoff_factor * (2 ** (retry_count - 1))), https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html
                        status_forcelist=[500, 502, 503, 504])
        s.mount('https://', HTTPAdapter(max_retries=retries))
        s.mount('http://', HTTPAdapter(max_retries=retries))
        # connect timeoutを10秒, read timeoutを30秒に設定
        r = s.request('GET', self.url, timeout=(10.0, 30.0))
        # ステータスコードが200番台以外だったら例外を起こす
        r.raise_for_status()
        return r


def main():
    url = 'http://localhost:5000'
    http_request = HttpRequest(url)
    try:
        response = http_request.request()
        # print(response.text)
    except requests.RequestException:
        print(f'request error {url}')


if __name__ == '__main__':
    main()
