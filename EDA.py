import pandas as pd
import numpy as np

def summary(df):
    print(f"Dataset has {df.shape[1]} features and {df.shape[0]} examples.")
    summary = df.describe().T
    summary.drop(columns=["count","25%","50%","75%"], inplace=True)
    summary["mode"] = df.mode().values[0]
    summary["median"] = df.median()
    summary["Unique"] = df.nunique().values
    summary["Missing"] = df.isnull().sum().values
    summary["Duplicated"] = df.duplicated().sum()
    summary["Types"] = df.dtypes
#     summary.drop(labels="id", inplace=True)
    return summary

data = pd.read_csv('/Users/lokeshrathi/PycharmProjects/Pandas-dev/input/kindey stone urine analysis.csv')

summary(data)
