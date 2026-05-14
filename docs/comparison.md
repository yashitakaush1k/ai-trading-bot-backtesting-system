Comparison: Backtest vs Paper Trading vs AI-Based Bot

## Purpose
This section compares the three strategy versions used in the project:
- Baseline moving-average backtest bot.
- Paper-trading / forward-test version.
- AI-based bot.

The goal is to see how the strategy performs under different testing conditions and whether the AI version improves performance.

## Interpretation
The baseline backtest shows the performance of the moving-average strategy on historical data. The paper-trading result is more realistic because it includes simulated execution, slippage, and fees. The AI-based bot should be compared against both to check whether it improves return, reduces drawdown, or lowers the number of bad trades.

## Observations from Paper Trading
The paper-trading run produced a large number of trades and a negative return. This suggests that the simple EMA crossover system is too sensitive and may be overtrading on noisy market data. Transaction costs and slippage had a strong negative effect on the final result.

## Conclusion
The comparison section shows that strategy performance should not be judged only by backtest profit. Paper trading is more realistic and helps reveal weaknesses that are hidden in historical tests. The AI-based bot should now be evaluated against this paper-trading baseline to see whether it produces better real-world behavior.

