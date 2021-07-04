import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class UrlRequest:
    def __init__(self, url):
        self.url = url

    def __del__(self) -> None:
        pass

    def request(self):
        s = requests.Session()
        retries = Retry(total=2,
                        backoff_factor=1,
                        status_forcelist=[500, 502, 503, 504])
        s.mount('https://', HTTPAdapter(max_retries=retries))
        s.mount('http://', HTTPAdapter(max_retries=retries))
        r = s.request('GET', self.url, timeout=(10.0, 30.0))
        r.raise_for_status()


def main():
    url = 'http://localhost:5000'
    url_request = UrlRequest(url)
    try:
        url_request.request()
    except requests.RequestException:
        print(f'request error {url}')


if __name__ == '__main__':
    main()
