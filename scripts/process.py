import pandas as pd
import numpy as np


def get_df_percent_missing(df: pd.DataFrame) -> str:
    totalCells = np.product(df.shape)
    missingCount = df.isnull().sum()
    totalMissing = missingCount.sum()
    return f"The telecom contains {round(((totalMissing/totalCells) * 100), 2)}% missing values."

def get_df_discribe(df:pd.DataFrame)->pd.DataFrame:
    return df.describe()

def get_df_null_count(df:pd.DataFrame)->pd.DataFrame:
    return df.isna().sum()

def get_df_information(df:pd.DataFrame)->pd.DataFrame:
    return df.info()

def get_missing_colum_percentage(df: pd.DataFrame) -> pd.DataFrame:
    num_missing = df.isnull().sum()
    num_rows = df.shape[0]

    data = {
        'num_missing': num_missing, 
        'percent_missing (%)': [round(x, 2) for x in num_missing / num_rows * 100]
    }

    stats = pd.DataFrame(data)

    # Filter columns with missing values
    return stats[stats['num_missing'] != 0]