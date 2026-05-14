System Architecture
The trading bot is built as a modular pipeline that processes historical market data, generates trade signals, simulates trades through a backtesting engine, and saves the final performance results. The overall design is meant to separate data handling, signal generation, trade execution logic, and performance analysis so that each part can be tested and improved independently.

High-Level Flow
Historical EUR/USD Data
→ Data Cleaning and Parsing
→ Feature/Signal Generation
→ Trading Logic
→ Backtesting Engine
→ Performance Metrics and Chart Output

Module Breakdown
1. Data Input Module
This module loads the historical EUR/USD CSV file from the data folder. The dataset contains bar-wise market information such as timestamp, open, high, low, close, and volume. The bot reads this data and converts it into a structured format so it can be processed reliably.

2. Data Cleaning Module
The raw CSV data is cleaned before any strategy is applied. In this step, the bot:

a.removes quotation marks and formatting issues
b.splits the data into proper columns
c.converts numeric columns into usable values
d.parses the datetime column
e.removes invalid or missing rows
f.sorts the data in chronological order
This step is important because trading logic depends on clean and correctly ordered historical data.

3. Signal Generation Module
This is the decision-making part of the bot. In the baseline version, the bot uses a technical rule based on moving averages. In the AI-based version, the Emergent component is intended to help interpret patterns and support trend-direction decisions before the final trading rule is applied.
The signal generation stage converts market data into buy and sell conditions. These signals define when the bot should enter or exit a trade.

4. Trading Logic Module
The trading logic determines how the bot behaves after a signal is generated. It defines:
a.when to open a position
b.when to close a position
c.how many units to buy or sell
d.and what happens if the market moves against the position
For this project, the logic is implemented in a rule-based manner so that the bot can be evaluated clearly in backtesting.

5. Backtesting Engine
The backtesting engine simulates how the bot would have performed on historical data. It does not place live trades. Instead, it:
a.enters and exits positions based on the signals
b.updates capital after each trade
c.tracks open positions
d.computes the equity curve over time
e.and records the total number of trades
This makes it possible to evaluate strategy performance without risking real money.

AI Component in the System
The AI-based part of the system is designed to improve or support signal generation by analyzing market patterns more intelligently than a simple rule-only approach. Instead of relying only on fixed moving-average conditions, the AI component can help interpret trend strength, market direction, or pattern behavior before a trade is taken.

This makes the AI-based version different from the baseline moving-average version in the following way:
a.The baseline version uses fixed technical rules only.
b.The AI-based version introduces pattern interpretation and adaptive decision support.
c.The AI layer is meant to make the strategy more flexible and less dependent on one static indicator.

Why This Architecture Was Chosen
This architecture was chosen because it is simple, modular, and easy to explain in a project report. It also allows the bot to be developed in stages:
a.start with data loading and cleaning
b.add strategy logic
c.test in backtest mode
d.compare with a baseline strategy
e.and later extend to paper trading or live-like simulation.

Summary
In short, the bot follows a clear pipeline:
a.historical data is loaded
b.data is cleaned
c.signals are generated
d.trades are simulated
e.and results are measured

This modular design makes the project easier to debug, easier to present, and easier to extend in the future.