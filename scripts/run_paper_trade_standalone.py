import pandas as pd
import matplotlib.pyplot as plt
from ta.trend import EMAIndicator
import os

BASE_DIR = r"C:\Users\YASHITA\OneDrive\Desktop\trading_bot_backtest"
FILE_PATH = os.path.join(BASE_DIR, "data", "EURUSD1.csv")
RESULT_PATH = os.path.join(BASE_DIR, "paper_equity_curve.png")
TRADES_CSV = os.path.join(BASE_DIR, "paper_trades.csv")

START_CAPITAL = 10000
FEE_RATE = 0.0001
SLIPPAGE = 0.00005

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
                rows.append([dt, parts[2], parts[3], parts[4], parts[5], parts[6]])
    return pd.DataFrame(rows, columns=["DateTime", "Open", "High", "Low", "Close", "Volume"])

def simulate_fill(side, price, units):
    slip = price * SLIPPAGE
    exec_price = price + slip if side == "BUY" else price - slip
    fee = exec_price * units * FEE_RATE
    return exec_price, fee

def run_paper_trade():
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

    capital = START_CAPITAL
    units = 0.0
    position = 0
    entry_price = 0.0
    equity = []
    trade_rows = []

    for i in range(len(df)):
        price = float(df.iloc[i]["Close"])
        ts = df.index[i]

        if df.iloc[i]["buy_signal"] and position == 0:
            units = capital / price
            exec_price, fee = simulate_fill("BUY", price, units)
            entry_price = exec_price
            capital -= fee
            position = 1
            trade_rows.append([ts, "BUY", price, exec_price, units, fee, 0.0, capital])

        elif df.iloc[i]["sell_signal"] and position == 1:
            exec_price, fee = simulate_fill("SELL", price, units)
            pnl = units * (exec_price - entry_price) - fee
            capital += pnl
            position = 0
            trade_rows.append([ts, "SELL", price, exec_price, units, fee, pnl, capital])
            units = 0.0
            entry_price = 0.0

        equity.append(capital + (units * price if position else 0.0))

    trades_df = pd.DataFrame(
        trade_rows,
        columns=["DateTime", "Side", "SignalPrice", "ExecPrice", "Units", "Fee", "PnL", "CapitalAfter"]
    )
    trades_df.to_csv(TRADES_CSV, index=False)

    final_capital = equity[-1] if equity else capital
    total_return = 100 * (final_capital - START_CAPITAL) / START_CAPITAL

    print("=== PAPER TRADING RESULTS ===")
    print(f"Final Capital: ${final_capital:.2f}")
    print(f"Total Return: {total_return:.2f}%")
    print(f"Trades Logged: {len(trades_df)}")
    print("Trades CSV saved as:", TRADES_CSV)

    plt.figure(figsize=(10, 6))
    plt.plot(equity)
    plt.title("Paper Trading Equity Curve")
    plt.xlabel("Bars")
    plt.ylabel("Equity")
    plt.grid(True)
    plt.savefig(RESULT_PATH)
    print("Result chart saved as:", RESULT_PATH)

if __name__ == "__main__":
    run_paper_trade()