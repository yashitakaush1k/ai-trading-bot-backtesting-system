
## Objective
The goal is to test the trading strategy in paper mode using simulated orders instead of real execution. This helps evaluate how the strategy behaves in a forward-testing environment while avoiding financial risk.

## Method
The existing EMA crossover strategy was reused from the backtest version. Real order execution was replaced with simulated fills that apply slippage and fees. Every trade was logged to a CSV file so the results could be analyzed later.

## Setup
The paper-trading script reads the same historical market data used in the backtest. It calculates EMA9 and EMA21, generates buy and sell signals, and then simulates order fills. The output files produced were:

- `paper_trades.csv`
- `paper_equity_curve.png`

## Trade Log Format
The paper-trade CSV contains the following columns:

- DateTime
- Side
- SignalPrice
- ExecPrice
- Units
- Fee
- PnL
- CapitalAfter

## Results
The paper-trading run produced the following summary:

- Buy signals: 2372
- Sell signals: 2372
- Trades Logged: 4744
- Final Capital: $4567.31
- Total Return: -54.33%

## Analysis
The paper-trading results show that the strategy is trading very frequently and losing money after slippage and fees. This suggests that the EMA crossover system is too noisy on this dataset and timeframe. The large number of trades also increases the impact of transaction costs.

## Conclusion
Phase 2 was completed successfully because the strategy was converted into a paper-trading version, trade logs were saved correctly, and the equity curve was generated. However, the current strategy performance is weak in forward-test mode, so further improvement is needed before any live deployment.

## Next Improvement
The next step is to reduce false signals by adding filters such as:
- RSI confirmation,
- trend-strength filtering,
- minimum candle distance between trades,
- or AI-based confirmation from the model.