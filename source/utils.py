import pandas as pd

def price_to_float(df: pd.DataFrame, column: str):
    """
    Transform price (str) to float by deleting '$' and ',' and changing dtype
    ----------
    Parameters:
    - df: dataframe
    - column: price column that needs transformation
    ----------
    Return: price column as type float
    """

    df['price_float'] = df[column].str.replace('$', '')
    df['price_float'] = df['price_float'].str.replace(',', '')
    df['price_float'] = df['price_float'].astype(float)

    return df


