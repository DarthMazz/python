import argparse
import re
import sys
from pathlib import Path


def get_args():
    parser = argparse.ArgumentParser()
    if sys.stdin.isatty():
        parser.add_argument("file", help="please set me", type=str)
    args = parser.parse_args()
    return (args)


def main():
    args = get_args()
    file_list_path = args.file
    folder_path = Path(file_list_path)
    for file in sorted(folder_path.glob('**/*.pdf')):
        if re.search('/\\d{4}/[a-z]{3}\\_?[a-z]{3}.pdf', str(file)):
            print(file)


if __name__ == '__main__':
    main()