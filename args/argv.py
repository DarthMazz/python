import sys


def analyze_argv(argv):
    """
    引数の解析

    Parameters
    ----------
    argv : string[]
        パラメータ

    Returns
    -------
    None
    """
    if len(argv) < 2:
        print("only python file.")
    else:
        print("some argv.")


if __name__ == "__main__":
    argv = sys.argv
    print(argv)
    analyze_argv(argv)
