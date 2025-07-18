# Momentum Trading Strategy Analysis with AutoGen

## Overview
This project implements a sophisticated momentum trading strategy analysis system using moving average (MA) crossovers. It leverages AutoGen's multi-agent framework to create a collaborative development environment where specialized AI agents work together to implement, test, and evaluate trading strategies.

The system analyzes different combinations of short and long-term moving averages to identify optimal parameters for momentum trading strategies on stock data. The current implementation focuses on NVIDIA (NVDA) but can be easily extended to other stocks and market instruments.

## Features

### Multi-agent Framework
Utilizes four specialized AI agents:
- **Code Generator**: Creates Python code for trading strategies
- **Code Executor**: Executes the generated code
- **Critic**: Evaluates the strategy implementation
- **Comparer**: Analyzes results across different parameter sets

### Momentum Strategy Implementation
- Moving average crossover-based momentum trading
- Support for different pairs of short and long window periods
- Buy/sell signal generation based on MA crossovers
- Performance metrics calculation (returns, Sharpe ratio, drawdowns)

### Comprehensive Analysis
- Comparative analysis of different MA pairs
- Visual representations of strategy performance
- Risk-return profiling
- Trading activity visualization

### Robust Data Handling
- Yahoo Finance data retrieval with automatic SSL handling
- Fallback data generation for testing
- Historical data processing and storage

## Installation

### Creating the Conda Environment
```bash
# Clone the repository
git clone https://github.com/danglive/momentum-trading-autogen.git
cd momentum-trading-autogen

# Create the Conda environment from the environment file
conda env create -f environment.yaml

# Activate the environment
conda activate momentum-trading
```

### Environment YAML File
The `environment.yaml` file contains all required dependencies:
```yaml
name: momentum-trading
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.10
  - pandas>=1.3.0
  - numpy>=1.20.0
  - matplotlib>=3.4.0
  - jupyter>=1.0.0
  - ipykernel>=6.0.0
  - ipywidgets>=7.6.0
  - seaborn>=0.11.0
  - pip
  - pip:
    - ag2>=0.2.0
    - yfinance>=0.1.70
```

## Project Structure
```
momentum-trading-autogen/
├── environment.yaml               # Conda environment specification
├── README.md                      # Project documentation
├── src/                           # Source code
│   ├── agents/                    # AutoGen agents
│   │   ├── __init__.py
│   │   ├── prompt_templates.py    # Agent prompt templates
│   │   └── setup_agents.py        # Agent initialization and setup
│   ├── strategies/                # Trading strategies
│   │   ├── __init__.py
│   │   └── momentum_trading_strategy.py  # Strategy implementation
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       └── data_utils.py          # Data handling utilities
├── notebooks/                     # Jupyter notebooks
│   ├── momentum_strategy_analysis.ipynb  # Basic strategy analysis
│   └── strategy_visualization.ipynb      # Visualization and comparison
├── examples/                      # Example scripts
│   ├── manual_momentum_analysis.py       # Manual analysis script
│   ├── momentum_cli.py                   # Command-line interface
│   ├── multi_pairs_momentum_analysis.py  # Multiple pairs analysis
│   └── multi_stock_analysis.py           # Multiple stocks analysis
└── output/                        # Output directory for results
```

## Usage

### Command Line Interface
```bash
# Analyze a single stock with one MA pair
python examples/momentum_cli.py single --symbol NVDA --short 5 --long 20

# Analyze a stock with multiple MA pairs
python examples/momentum_cli.py pairs --symbol AAPL

# Analyze multiple stocks with one MA pair
python examples/momentum_cli.py stocks --short 10 --long 50
```

### Jupyter Notebooks
```bash
# Start Jupyter Notebook
jupyter notebook notebooks/strategy_visualization.ipynb
```

### Python API
```python
from src.utils.data_utils import download_stock_data
from src.strategies.momentum_trading_strategy import run_strategy_analysis

# Download stock data
df = download_stock_data("NVDA", "2024-01-01", "2024-11-08")

# Run strategy analysis
results = run_strategy_analysis(
    df,
    short_window=5,
    long_window=20,
    symbol="NVDA",
    save_results=True,
    output_dir="output"
)

# Print results
print(f"Final return: {results['final_return']:.2%}")
```

### Using AutoGen Multi-Agent Framework
```python
from src.agents import create_agents, run_momentum_analysis

# Create agents
agents = create_agents(api_key="YOUR_OPENAI_API_KEY")

# Run momentum analysis
result = run_momentum_analysis(
    agents,
    symbol="NVDA",
    start_date="2024-01-01",
    end_date="2024-11-08",
    ma_pairs=[(5, 20), (10, 50), (20, 100), (50, 200)]
)
```

## Troubleshooting

### SSL Certificate Issues
```python
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
```

### No Data Available
- Check your internet connection
- Verify the date range is valid
- Try a different data source or API

### AutoGen Issues
- Ensure your OpenAI API key is valid and set correctly
- Check if you have sufficient API credits
- Try upgrading to the latest version of `ag2`

## Performance Metrics
- **Total Return**: The final cumulative return of the strategy
- **Sharpe Ratio**: Risk-adjusted return (higher is better)
- **Maximum Drawdown**: Largest peak-to-trough decline (lower is better)
- **Trading Frequency**: Number of buy/sell signals generated

## Extending the Project

### Adding New Strategies
```python
# src/strategies/rsi_strategy.py
def calculate_rsi(prices, period=14):
    ...

def rsi_strategy(df, oversold=30, overbought=70):
    ...
```

### Supporting Additional Data Sources
```python
def download_alpha_vantage_data(symbol, api_key, start_date, end_date):
    ...
```

### Creating Custom Agents
```python
# src/agents/optimizer_agent.py
from autogen import AssistantAgent

def create_optimizer_agent(config_list):
    return AssistantAgent(
        name="Optimizer",
        system_message="You are an expert in optimizing trading strategies...",
        llm_config={"config_list": config_list}
    )
```

## Interactive Dashboard

The project includes an interactive Streamlit dashboard for visualizing and analyzing momentum trading strategies.

### Dashboard Features

- **Multiple Analysis Types**:
  - Single Pair Analysis: Examine one stock with a specific MA pair
  - Multiple Pairs Analysis: Compare different MA pairs for one stock
  - Multiple Stocks Analysis: Compare different stocks with the same MA pair
  
- **Interactive Controls**:
  - Stock symbol selection
  - Date range selection
  - MA parameter configuration with sliders
  - Custom MA pair addition
  - Multiple stocks selection

- **Comprehensive Visualizations**:
  - Price charts with MA lines and buy/sell signals
  - Portfolio performance comparison (strategy vs buy & hold)
  - Returns comparison across different MA pairs or stocks
  - Cumulative returns visualization

- **Performance Metrics**:
  - Total return
  - Sharpe ratio
  - Maximum drawdown
  - Win rate

### Running the Dashboard

To run the interactive dashboard:

```bash
# Install Streamlit if not already installed
pip install streamlit plotly

# Launch the dashboard
streamlit run app.py

## Disclaimer
This project is intended for educational purposes only and is not financial advice. Trading involves risk, and past performance is not indicative of future results. Always consult a qualified financial advisor before making investment decisions.