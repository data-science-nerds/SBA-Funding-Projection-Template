import pandas as pd


def ingest_data(raw_data_file: str) -> pd.DataFrame:
    # Load the data from the Excel file
    excel_data = pd.read_excel(f'{raw_data_file}') 
    print(excel_data.head())
    return excel_data


def main_data_flow(raw_data_file: str) -> pd.DataFrame:
    df = ingest_data(raw_data_file)
    return df

if __name__ == "__main__":
    data = main_data_flow(raw_data_file)