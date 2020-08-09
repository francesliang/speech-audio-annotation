import os
import pandas as pd


def split_data(tsv_file, out_dir, train=0.7, dev=0.2, test=0.1):
    df = pd.read_csv(tsv_file, sep='\t')
    df = df.dropna()
    total = len(df.index)
    train_num = int(total * train)
    dev_num = int(total * dev)
    test_num = int(total * test)

    # Shuffle dataframe rows
    df = df.sample(frac=1).reset_index(drop=True)

    if total < 10:
        train_df = df
        dev_df = df
        test_df = df
    else:
        train_df = df[0:train_num]
        dev_df = df[train_num:(train_num + dev_num)]
        test_df = df[(train_num + dev_num):]

    # Write data to files
    train_df.to_csv(os.path.join(out_dir, "train.tsv"), sep='\t')
    dev_df.to_csv(os.path.join(out_dir, "dev.tsv"), sep='\t')
    test_df.to_csv(os.path.join(out_dir, "test.tsv"), sep='\t')

