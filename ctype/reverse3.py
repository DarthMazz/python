import timeit
import ctypes

lib = ctypes.cdll.LoadLibrary('./lib3.so')
lib.reverse_str.argtypes = (ctypes.c_int, ctypes.c_wchar_p)  # 型が変わる
lib.reverse_str.restype = ctypes.c_wchar_p


def reverse_str(buf):
    n = len(buf)
    result = lib.reverse_str(n, buf)
    lib.free_result()
    return result


if __name__ == "__main__":
    s = "hogefugaほげふが"*(10**3)
    print(s[::-1] == reverse_str(s))
    print(timeit.timeit(lambda : reverse_str(s), number=10**3))
    print(timeit.timeit(lambda : s[::-1], number=10**3))
