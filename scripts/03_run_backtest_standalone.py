import pandas as pd
import matplotlib.pyplot as plt
from ta.trend import EMAIndicator
import os

BASE_DIR = r"C:\Users\YASHITA\OneDrive\Desktop\trading_bot_backtest"
FILE_PATH = os.path.join(BASE_DIR, "data", "EURUSD1.csv")
RESULT_PATH = os.path.join(BASE_DIR, "equity_curve.png")

def load_manual_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip().replace('"', '')
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 7:
                dt = parts[0] + " " + parts[1]
                open_p = parts[2]
                high_p = parts[3]
                low_p = parts[4]
                close_p = parts[5]
                vol = parts[6]
                rows.append([dt, open_p, high_p, low_p, close_p, vol])

    return pd.DataFrame(rows, columns=["DateTime", "Open", "High", "Low", "Close", "Volume"])

def run_full_backtest():
    print("Looking for file at:", FILE_PATH)

    if not os.path.exists(FILE_PATH):
        print("ERROR: Cannot find CSV file.")
        return

    df = load_manual_csv(FILE_PATH)

    df["DateTime"] = pd.to_datetime(df["DateTime"], format="%Y-%m-%d %H:%M", errors="coerce")
    for col in ["Open", "High", "Low", "Close", "Volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.dropna(inplace=True)
    df.set_index("DateTime", inplace=True)
    df.sort_index(inplace=True)

    df["EMA9"] = EMAIndicator(df["Close"], window=9).ema_indicator()
    df["EMA21"] = EMAIndicator(df["Close"], window=21).ema_indicator()
    df.dropna(subset=["EMA9", "EMA21"], inplace=True)

    df["buy_signal"] = (df["EMA9"] > df["EMA21"]) & (df["EMA9"].shift(1) <= df["EMA21"].shift(1))
    df["sell_signal"] = (df["EMA9"] < df["EMA21"]) & (df["EMA9"].shift(1) >= df["EMA21"].shift(1))

    print("Buy signals:", int(df["buy_signal"].sum()))
    print("Sell signals:", int(df["sell_signal"].sum()))

    capital = 10000
    units = 0
    position = 0
    entry_price = 0
    equity = []
    trades = []

    for i in range(len(df)):
        price = df.iloc[i]["Close"]

        if df.iloc[i]["buy_signal"] and position == 0:
            units = capital / price
            position = 1
            entry_price = price
            trades.append(("BUY", df.index[i], price))

        elif df.iloc[i]["sell_signal"] and position == 1:
            pnl = units * (price - entry_price)
            capital += pnl
            position = 0
            trades.append(("SELL", df.index[i], price, pnl))

        equity.append(capital + (units * price if position else 0))

    print("=== BACKTEST RESULTS ===")
    print(f"Final Capital: ${capital:.2f}")
    print(f"Total Return: {100*(capital-10000)/10000:.2f}%")
    print(f"Trades: {len(trades)}")

    plt.figure(figsize=(10, 6))
    plt.plot(equity)
    plt.title("Equity Curve")
    plt.xlabel("Bars")
    plt.ylabel("Equity")
    plt.grid(True)
    plt.savefig(RESULT_PATH)
    print("Result chart saved as:", RESULT_PATH)

if __name__ == "__main__":
    run_full_backtest()