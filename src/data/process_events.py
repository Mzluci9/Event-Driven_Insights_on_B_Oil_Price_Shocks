# Feature Engineering: Generating New Variables for Prediction

import pandas as pd
import numpy as np

def read_brent_prices(csv_path):
    """
    Import Brent crude oil price data from a CSV file.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded dataset with Date as datetime64.
    """
    df = pd.read_csv(csv_path)
    # Parse dates with mixed formats
    df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True, errors='coerce')
    if df['Date'].isnull().any():
        print("[WARNING] Some dates could not be parsed and are set to NaT.")
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
    print(f"[INFO] Removed {len(df) - len(df_cleaned)} rows with missing data.")
    df_cleaned = df_cleaned.reset_index(drop=True)
    print("[INFO] Index has been reset.")
    return df_cleaned

def engineer_features(df, ma_windows=[30, 90], std_windows=[30, 90], lag_days=[1, 7, 30]):
    """
    Engineer features for Brent oil price data, including moving averages, rolling std, lags, and log returns.
    
    Parameters:
    - df: DataFrame with 'Date' (datetime64) and 'Price' columns
    - ma_windows: List of moving average window sizes (e.g., [30, 90])
    - std_windows: List of rolling standard deviation window sizes
    - lag_days: List of lag periods (e.g., [1, 7, 30])
    
    Returns:
    - DataFrame with engineered features
    """
    df = df.copy()
    # Ensure Date is datetime (should already be from read_brent_prices)
    if not pd.api.types.is_datetime64_any_dtype(df['Date']):
        raise ValueError("Date column must be datetime64 type")
    df = df.sort_values('Date').reset_index(drop=True)
    
    # Ensure Price is numeric and handle missing values
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Price'] = df['Price'].fillna(method='ffill')
    
    # Moving Averages
    for window in ma_windows:
        df[f'Price_MA{window}'] = df['Price'].rolling(window=window, min_periods=1).mean()
    
    # Rolling Standard Deviations
    for window in std_windows:
        df[f'Price_Rolling_STD{window}'] = df['Price'].rolling(window=window, min_periods=1).std()
    
    # Lagged Prices
    for lag in lag_days:
        df[f'Price_Lag{lag}'] = df['Price'].shift(lag)
    
    # Log Returns
    df['Log_Returns'] = np.log(df['Price']).diff()
    
    # Drop rows with NaN values in lagged columns
    df = df.dropna().reset_index(drop=True)
    
    # Round numerical columns to 6 decimal places
    numeric_cols = [col for col in df.columns if col != 'Date']
    df[numeric_cols] = df[numeric_cols].round(6)
    
    return df

if __name__ == "__main__":
    # Define file location
    csv_path = 'C:/Users/HP/10 Acadamy PRojects/New folder (10)/Event-Driven_Insights_on_B_Oil_Price_Shocks/data/raw/BrentOilPrices.csv'

    # Step 1: Load data
    brent_df = read_brent_prices(csv_path)

    # Step 2: Examine structure and nulls
    inspect_dataset(brent_df)

    # Step 3: Clean data
    cleaned_df = preprocess_brent_data(brent_df)

    # Step 4: Engineer features
    engineered_df = engineer_features(cleaned_df)

    # Step 5: Preview engineered data
    print("\n=== Sample of Engineered Data ===")
    print(engineered_df.head())

    # Save to processed data folder
    output_path = 'C:/Users/HP/10 Acadamy PRojects/New folder (10)/Event-Driven_Insights_on_B_Oil_Price_Shocks/data/processed/brent_engineered_features.csv'
    engineered_df.to_csv(output_path, index=False)
    print(f"[INFO] Engineered data saved to {output_path}")