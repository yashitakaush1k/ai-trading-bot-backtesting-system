import pandas as pd
from ta.trend import EMAIndicator

def add_ema_signals(df):
    """Add EMA9/EMA21 and crossover signals"""
    
    # Calculate EMAs
    df['EMA9'] = EMAIndicator(df['Close'], window=9).ema_indicator()
    df['EMA21'] = EMAIndicator(df['Close'], window=21).ema_indicator()
    
    # Crossover logic
    df['ema9_above_ema21'] = df['EMA9'] > df['EMA21']
    df['prev_ema9_above_ema21'] = df['ema9_above_ema21'].shift(1)
    
    # Buy signal: EMA9 crosses above EMA21
    df['buy_signal'] = df['ema9_above_ema21'] & ~df['prev_ema9_above_ema21']
    
    # Sell signal: EMA9 crosses below EMA21
    df['sell_signal'] = ~df['ema9_above_ema21'] & df['prev_ema9_above_ema21']
    
    print("Sample signals:")
    print(df[['Close', 'EMA9', 'EMA21', 'buy_signal', 'sell_signal']].tail(10))
    
    return df

if __name__ == "__main__":
    from data_loader import load_data  # adjust path if needed
    df = load_data("../data/eurusd_1h.csv")
    df = add_ema_signals(df)