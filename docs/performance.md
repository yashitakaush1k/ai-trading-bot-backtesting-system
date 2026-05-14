Performance

Overview
- This section reports key backtest results required for the report: total return, number of trades, win rate, max drawdown, and (optional) Sharpe ratio. 

Metric definitions
- Total return — cumulative percentage return over the backtest period (end equity / start equity − 1).
- Number of trades — total executed trades (entries or round-trip trades; specify which convention you use).
- Win rate — percentage of trades that were profitable (winning trades / total trades).
- Max drawdown — maximum peak-to-trough decline in equity during the backtest, expressed as a percentage.
- Sharpe ratio (optional) — annualized excess return divided by annualized volatility, typically using a risk-free rate of 0% for short-term strategies; formula: Sharpe = (mean(returns) − rf) / std(returns) annualized. 

How to compute (practical notes)
- Use the same equity series for all metrics (start-to-end equity after P&L, fees, and slippage).
- Count trades consistently: use round-trips (entry+exit = 1 trade) unless you document otherwise.
- For max drawdown, compute running peak of equity and the largest percentage drop to a subsequent trough.
- For Sharpe, compute returns at the same periodicity (daily returns for daily series), then annualize: annualized mean = mean(daily_returns) * 252, annualized std = std(daily_returns) * sqrt(252).


flowchart LR
  EQ[Equity curve CSV] --> CALC[Compute metrics\n(total return, max drawdown, Sharpe)]
  TL[Trade log CSV] --> CALC2[Compute metrics\n(num trades, win rate, avg P&L)]
  CALC --> REPORT[Performance table]
  CALC2 --> REPORT