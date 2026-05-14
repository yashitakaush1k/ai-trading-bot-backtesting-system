import pandas as pd

def load_data(filepath):
    """Load OHLCV data from CSV"""
    df = pd.read_csv(filepath)
    
    # Convert timestamp to datetime (adjust column name if needed)
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # change 'timestamp' to your actual column name
    df.set_index('timestamp', inplace=True)
    
    # Sort by time
    df.sort_index(inplace=True)
    
    print(f"Loaded {len(df)} rows from {filepath}")
    print(df.head())
    return df

if __name__ == "__main__":
    df = load_data("../data/eurusd_1h.csv")