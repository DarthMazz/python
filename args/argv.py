import sys
import argparse


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


def get_args():
    """
    引数取得

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    parser = argparse.ArgumentParser()

    if sys.stdin.isatty():
        parser.add_argument("file", help="please set me", type=str)

    parser.add_argument("--type", type=int)
    parser.add_argument("--alert", help="optional", action="store_true")

    args = parser.parse_args()

    return (args)


def main():
    """
    メイン処理
    """
    args = get_args()

    if hasattr(args, 'file'):
        print(args.file)
    print(args.type)
    print(args.alert)

    if args.alert:
        None


if __name__ == "__main__":
    argv = sys.argv
    print(argv)
    analyze_argv(argv)
    main()
