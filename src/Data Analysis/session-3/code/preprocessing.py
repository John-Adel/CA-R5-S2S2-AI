import pandas as pd


def read_files(file_path):
    return pd.read_csv(file_path)


def drop_cols(df, cols):
    return df.drop(columns=cols)


def get_type_info(df):
    return pd.DataFrame({"dtypes": df.dtypes, "nunique": df.nunique()}).T

def replace_outliers(df):
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_fence = Q1 - (1.5 * IQR)
        upper_fence = Q3 + (1.5 * IQR)

        df[col] = df[col].clip(lower_fence, upper_fence)
    return df