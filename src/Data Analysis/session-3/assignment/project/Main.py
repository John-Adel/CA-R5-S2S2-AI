from preprocessing import *
from config.config import *
import pandas as pd
df = read_data_file(file_path)
df = drop_unnecessary_features(df, cols_to_drop)
print(check_data_type(df))