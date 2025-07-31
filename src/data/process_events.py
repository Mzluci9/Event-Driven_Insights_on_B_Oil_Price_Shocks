import pandas as pd

def read_brent_prices(csv_path):
    """
    Import Brent crude oil price data from a CSV file.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded dataset.
    """
    df = pd.read_csv(csv_path, parse_dates=['Date'], dayfirst=True)
    print("[INFO] Data successfully read from file.")
    return df

def inspect_dataset(df):
    """
    Display column data types and missing value counts.

    Args:
        df (pd.DataFrame): The dataset to inspect.

    Returns:
        None
    """
    print("=== Column Data Types ===")
    print(df.dtypes)

    print("\n=== Missing Values Summary ===")
    print(df.isnull().sum())

def preprocess_brent_data(df):
    """
    Clean Brent price data by removing null rows and resetting the index.

    Args:
        df (pd.DataFrame): Raw dataset.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    df_cleaned = df.dropna()
    print("[INFO] Removed rows with missing data.")

    df_cleaned.reset_index(drop=True, inplace=True)
    print("[INFO] Index has been reset.")

    return df_cleaned

if __name__ == "__main__":
    # Define file location
    csv_path = 'C:/Users/HP/10 Acadamy PRojects/New folder (10)/Event-Driven_Insights_on_B_Oil_Price_Shocks/data/raw/BrentOilPrices.csv'

    # Step 1: Load data
    brent_df = read_brent_prices(csv_path)

    # Step 2: Examine structure and nulls
    inspect_dataset(brent_df)

    # Step 3: Clean data
    cleaned_df = preprocess_brent_data(brent_df)

    # Step 4: Preview cleaned result
    print("\n=== Sample of Cleaned Data ===")
    print(cleaned_df.head())
