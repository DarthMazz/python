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


def concat_df(df1, df2):
    return pd.concat([df1, df2])


def read_csvfile(csvfile):
    df = pd.read_csv(csvfile)
    print('----- df -----')
    print(df)
    print('----- df.dtypes -----')
    print(df.dtypes)
    df_rename = df.rename(columns={'binalize': 'binalize_after'})
    print('----- df.rename -----')
    print(df_rename)
    # print('----- df.concat -----')
    # print(concat_df(df, df_rename))
    df_suffix = df.add_suffix('_after')
    print('----- df.add_suffix -----')
    print(df_suffix)
    df_concat = pd.concat([df, df_rename])
    print('----- df.concat -----')
    print(df_concat)
    grouped = df_concat.groupby('filename')
    print('----- grouped.mean() -----') # 平均
    print(grouped.mean())
    print('----- grouped.describe() -----')
    print(grouped.describe())
    print('----- grouped.max() -----')
    print(grouped.max())
    print('----- grouped.max - min -----')
    print(grouped.agg(lambda x: max(x) - min(x)))
    print('----- grouped maen(average) max min -----')
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
