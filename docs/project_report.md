Comparison: Baseline vs AI-based Bot

Purpose
- Keep both implementations (baseline moving-average bot and AI-based bot) and compare them on the same backtest dataset and period to ensure a fair experiment.  
- Compare these core metrics: total return, number of trades, win rate, max drawdown, and optionally Sharpe ratio.  

Evaluation protocol
- Use the same time window, instruments, transaction cost model, slippage assumptions, and position-sizing rules for both runs.  
- Use the same data versions and preprocessing pipeline so any difference is caused by strategy logic only.  
- Prefer walk‑forward or repeated out‑of‑sample windows and report mean ± confidence intervals rather than single-run numbers when possible.  

Suggested additional diagnostics
- Trade distribution: compare P&L per trade histograms and mean/median P&L.  
- Exposure & turnover: show average position size, average holding time, and turnover; AI may trade less/more frequently.  
- Regime breakdown: compute metrics by market regime (bull, bear, high volatility) to see where AI helps or hurts.  
- Signal overlap: measure how often AI and MA produce the same signal (agreement rate) and cases where AI filters MA crossovers.

Interpretation checklist
- Higher total return and Sharpe with similar or lower max drawdown indicates a meaningful improvement.  
- If win rate improves but total return doesn’t, inspect average loss size — large losses can wipe out more wins.  
- If AI reduces false signals (fewer small losing trades) but increases exposure length, verify risk-adjusted returns.  
- If number of trades differs substantially, check transaction costs impact — simulate fees and slippage.  

Simple statistical test (recommended)
- Use a paired test across walk‑forward windows or bootstrap resampling of returns to test whether return differences are statistically significant (e.g., paired t-test or bootstrap CI for difference in mean return).  
- Report p‑values or confidence intervals alongside means to avoid over-interpreting noise.

Quick checklist before declaring a winner
- Same data and cost assumptions used.  
- Results stable across multiple windows (not just one cherry-picked period).  
- Improvement survives realistic transaction costs and slippage.  
- Monitoring plan in place if the AI bot is promoted to paper/canary/live trading.

