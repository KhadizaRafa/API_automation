import pandas as pd


def read_test_data(filepath):
    return pd.read_excel(filepath)

def write_results(dataframe, output_path):
    dataframe.to_excel(output_path, index=False)

def convert_excel_to_json(filepath):
    df = pd.read_excel(filepath, engine='openpyxl')
    return df.to_dict(orient="records")  # List of dictionaries
