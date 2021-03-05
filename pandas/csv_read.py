import argparse
import matplotlib
import pandas as pd
import sys


def get_args():
    parser = argparse.ArgumentParser()
    if sys.stdin.isatty():
        parser.add_argument("csvfile", help="please set me", type=str)
    args = parser.parse_args()
    return (args)


def read_csvfile(csvfile):
    df = pd.read_csv(csvfile)
    print(df)
    print(df.dtypes)
    grouped = df.groupby('filename')
    print(grouped.mean())
    print(grouped.describe())
    print(grouped.max())
    print(grouped.agg(lambda x: max(x) - min(x)))
    print(grouped.agg(['mean', max, min]))
    grouped.agg(['mean', max, min]).to_csv('to_csv_out.csv')
    ax = grouped.max().plot.bar(rot=0)
    fig = ax.get_figure()
    fig.savefig('filename_groupby_max.jpg')


def main():
    args = get_args()
    read_csvfile(args.csvfile)


if __name__ == '__main__':
    main()
