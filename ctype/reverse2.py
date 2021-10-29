import ctypes

lib = ctypes.cdll.LoadLibrary('./lib2.so')
lib.reverse_bytes.argtypes = (ctypes.c_int, ctypes.c_char_p)  # 型が変わる
lib.reverse_bytes.restype = ctypes.c_char_p


def reverse_bytes(buf):
    n = len(buf)
    result = lib.reverse_bytes(n, buf)
    lib.free_result()
    return result


if __name__ == "__main__":
    print(reverse_bytes(b"hoge"))
