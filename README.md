# Binance Futures Testnet Trading Bot

A simplified trading bot built using Python for Binance Futures Testnet (USDT-M).

This project was created as part of a backend engineering assignment focused on API integration, modular backend design, validation, logging, and error handling.

The bot supports:
- MARKET orders
- LIMIT orders
- BUY and SELL operations
- CLI interaction
- Streamlit UI testing

---

# Features

- Binance Futures Testnet integration
- MARKET and LIMIT order support
- BUY / SELL support
- CLI-based interaction using Typer
- Lightweight Streamlit UI
- Input validation
- Error handling
- Logging system
- Modular backend structure

---

# Tech Stack

- Python
- python-binance
- Streamlit
- Typer
- python-dotenv
- Rich

---

# Project Structure

```txt
trading_bot/
 ├── bot/
 │    ├── client.py
 │    ├── orders.py
 │    ├── validators.py
 │    ├── logging_config.py
 │
 ├── logs/
 │
 ├── screenshots/
 │
 ├── cli.py
 ├── app.py
 ├── README.md
 ├── requirements.txt
 ├── .gitignore
 ├── .env

Installation
Clone Repository
git clone https://github.com/srigayatrii/binance-futures-testnet-bot.git
cd binance-futures-testnet-bot

Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Running the CLI
MARKET Order
python cli.py BTCUSDT BUY MARKET 0.001
LIMIT Order
python cli.py BTCUSDT SELL LIMIT 0.001 --price 95000

The CLI validates:
order side
order type
quantity
LIMIT order pricing
before placing orders.

Running the Streamlit UI
streamlit run app.py

The UI supports:
symbol input
BUY / SELL selection
MARKET / LIMIT order placement
quantity validation
LIMIT price input

Logging
Logs are automatically stored in:
logs/trading_bot.log

The logger tracks:
order requests
successful responses
validation failures
API/runtime errors

Screenshots of:
successful CLI orders
Streamlit UI
successful API responses
are included in the screenshots/ folder.

Validation Implemented

Invalid BUY/SELL prevention
Invalid order type prevention
Quantity validation
LIMIT order price validation

Development Notes
The application was initially developed using a mock order flow before integrating with the live Binance Futures Testnet API.
This helped isolate validation logic, logging behavior, and application structure before external API integration.

Assumptions
Binance Futures Testnet account is active
Valid API credentials are available
Python 3.10+ is installed
