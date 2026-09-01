import pandas as pd
try:
    def read_data_file(file_path: str) -> pd.DataFrame:
        '''  This function only reads csv files

        


        Args:
            file_path: The path of the csv file you want to read

        Returns:
            A DataFrame
        '''
        if not file_path.endswith(".csv"):
            raise TypeError("This is not a csv file")
        else:
            return pd.read_csv(file_path)
except FileNotFoundError:
    print("This file doesn't exist")


def drop_unnecessary_features(df, cols_to_drop):
    return df.drop(cols_to_drop, axis = 1)

df = pd.DataFrame()
def check_data_type(df):
    output = pd.DataFrame(columns= ["Name", "Data Type", "Unique"])
    for col in df.columns:
        output.loc[len(output)] = [df[col].name, df[col].dtype, df[col].nunique()]
    return output.T

