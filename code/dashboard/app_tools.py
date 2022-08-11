import pandas as pd

def subset_chart(df, col, value):
    """
    """
    df_subset = df[df[col]==value]

    return df_subset