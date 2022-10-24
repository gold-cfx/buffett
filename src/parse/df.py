import pandas as pd
from pandas import DataFrame


def add_col_by_multiplication(df: DataFrame, col1, col2, new_col_name):
    df[[col1, col2]] = df[[col1, col2]].astype(float)
    df[new_col_name] = df[col1] * df[col2]
    return df


def add_col_by_func(df: DataFrame, col1, new_col_name, slice_func, col1_type):
    df[[col1]] = df[[col1]].astype(col1_type)
    df[new_col_name] = df[col1].apply(slice_func)
    return df


def add_col_by_group_sum(df: DataFrame, col1, *sum_col):
    agg_fun = {}
    for col in sum_col:
        agg_fun[col] = "sum"
    df = df.groupby(col1, as_index=False).agg(agg_fun)
    return df


def add_col_by_group_undefined(df: DataFrame, col1, agg_func):
    df = df.groupby(col1, as_index=False).apply(agg_func)
    return df


def my_agg(x):
    names = {
        'Total_Count': x['Type'].count(),
        'Total_Number': x['Number'].sum(),
        'Count_Status=Y': x[x['Status'] == 'Y']['Type'].count(),
        'Number_Status=Y': x[x['Status'] == 'Y']['Number'].sum(),
        'Count_Status=N': x[x['Status'] == 'N']['Type'].count(),
        'Number_Status=N': x[x['Status'] == 'N']['Number'].sum()
    }

    return pd.Series(names)
