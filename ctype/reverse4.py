import ctypes

lib = ctypes.cdll.LoadLibrary('./lib44.so')
lib.reverse_bytes.argtypes = (ctypes.c_int, ctypes.c_char_p)  # 型が変わる
lib.reverse_bytes.restype = ctypes.c_int


def reverse_bytes(buf):
    n = len(buf)
    result = lib.reverse_bytes(n, buf)
    return result


if __name__ == "__main__":
    print(reverse_bytes(b"./README.md"))
    filename = './README.md'
    print(reverse_bytes(filename.encode()))
    filename = './リードミー.md'
    print(reverse_bytes(filename.encode()))
