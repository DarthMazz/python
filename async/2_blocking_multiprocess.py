import socket
import time
from concurrent.futures import ProcessPoolExecutor


def blocking_way():
    sock = socket.socket()
    # blocking
    sock.connect(('example.com', 80))
    request = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response


def multi_process_way():
    with ProcessPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(blocking_way) for i in range(10)}
    return len([future.result() for future in futures])


if __name__ == '__main__':
    elapsed_times = 0
    for _ in range(10):
        start = time.time()
        multi_process_way()
        elapsed_time = time.time() - start
        elapsed_times += elapsed_time
        print(f"elapsed_time: {(elapsed_time):.2f}[sec]")
    print(f"mean_elapsed_time: {(elapsed_times/10):.2f}[sec]")