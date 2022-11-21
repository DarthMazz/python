import socket
import time
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ


class Crawler:
    def __init__(self, path):
        self.path = path
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('example.com', 80))
        except BlockingIOError:
            pass
        selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key, mask):
        selector.unregister(key.fd)
        get = f'GET {self.path} HTTP/1.0\r\nHost: example.com\r\n\r\n'
        self.sock.send(get.encode('ascii'))
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stopped
        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            paths_todo.remove(self.path)
            if not paths_todo:
                stopped = True


def loop():
    while not stopped:
        # 何らかのイベントが発生するまでブロッキングする
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)


if __name__ == '__main__':
    elapsed_times = 0
    for _ in range(10):
        selector = DefaultSelector()
        stopped = False
        paths_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}
        start = time.time()
        for path in paths_todo:
            crawler = Crawler(path)
            crawler.fetch()
        loop()
        elapsed_time = time.time() - start
        elapsed_times += elapsed_time
        print(f"elapsed_time: {(elapsed_time):.2f}[sec]")
    print(f"mean_elapsed_time: {(elapsed_times/10):.2f}[sec]")