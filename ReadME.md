# AI Trading Bot Backtesting & Paper Trading System

## Project Overview
This project is a complete algorithmic trading system built in Python that performs:

* Historical backtesting on forex market data
* Strategy evaluation and performance analysis
* Paper trading (simulated live trading)
* Equity curve visualization
* Trade logging and result comparison

The project demonstrates the full workflow of quantitative trading system development, from data loading and strategy testing to forward testing through paper trading.

---

# Features

## Backtesting Engine
* Loads historical market data from CSV files
* Applies a custom trading strategy
* Simulates trade execution
* Calculates profit/loss and account equity
* Generates equity curve charts

## Paper Trading System
* Reuses the same trading logic from the backtest
* Simulates live order execution without risking real money
* Logs all paper trades into CSV files
* Tracks forward performance over time

## Performance Tracking
* Equity curve visualization
* Trade logs for analysis
* Strategy comparison reports
* Forward testing support

## Documentation
* Modular project structure
* Separate scripts and documentation folders
* Markdown documentation for architecture and reports

---

# Project Structure

```bash
trading_bot_backtest/
│
├── data/
│   └── EURUSD1.csv
│
├── docs/
│   ├── AI_component.md
│   ├── architecture.md
│   ├── backtest_and_pipeline.md
│   ├── comparison.md
│   ├── paper_trading.md
│   ├── performance.md
│   └── project_report.md
│
├── results/
│   ├── equity_curve.png
│   ├── paper_equity_curve.png
│   └── paper_trades.csv
│
├── scripts/
│   ├── 01_data_loader.py
│   ├── 02_strategy.py
│   ├── 03_run_backtest_standalone.py
│   └── run_paper_trade_standalone.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* yfinance

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-trading-bot.git
cd ai-trading-bot
```

## 2. Create a Virtual Environment 

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements
```txt
pandas
numpy
matplotlib
scikit-learn
yfinance
```
---

# Running the Project

## Run Backtest

```bash
python scripts/03_run_backtest_standalone.py
```
---

## Run Paper Trading Simulation

```bash
python scripts/run_paper_trade_standalone.py
```
---

# Outputs

## Backtest Outputs

* `equity_curve.png`
* Performance statistics
* Trade execution logs

## Paper Trading Outputs

* `paper_trades.csv`
* `paper_equity_curve.png`

These outputs are stored inside the `results/` folder.

---

# Strategy Workflow

1. Load historical market data
2. Preprocess and clean data
3. Apply trading signals
4. Execute simulated trades
5. Calculate profit/loss
6. Track equity growth
7. Generate reports and charts
8. Run paper trading for forward testing

---

# Forward Testing

The project includes a paper trading module that acts as a forward testing environment.

Instead of executing real trades:

* Orders are simulated
* Trades are logged locally
* Strategy performance is tracked over time

This helps validate strategy robustness before real deployment.

---

# Future Improvements

Possible future upgrades:

* Real broker API integration
* Live trading execution
* Risk management module
* Stop-loss and take-profit automation
* Multi-asset support
* Machine learning signal generation
* Dashboard/UI for monitoring
* Docker deployment
* Cloud hosting

---

# Learning Outcomes

This project demonstrates:

* Quantitative finance concepts
* Backtesting system design
* Paper trading simulation
* Python data analysis
* Financial data visualization
* Modular software architecture
* Research and experimentation workflow

---

# Author

Yashita Kaushik

GitHub: [https://github.com/your-username](https://github.com/your-username)

---

# License

This project is for educational and research purposes.

# Sample Results

## Backtest Equity Curve

![Backtest Equity Curve](results/equity_curve.png)

---

## Paper Trading Equity Curve

![Paper Trading Equity Curve](results/paper_equity_curve.png)