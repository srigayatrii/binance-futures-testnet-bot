import streamlit as st
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

st.set_page_config(
    page_title="Trading Bot",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Binance Futures Testnet Bot")

st.markdown(
    "Place MARKET and LIMIT orders "
    "using Binance Futures Testnet."
)

with st.sidebar:
    st.header("Bot Information")

    st.success("Environment: TESTNET")

    st.write(
        """
        Supported Features:
        - BUY / SELL
        - MARKET orders
        - LIMIT orders
        - Validation
        - Logging
        """
    )

st.subheader("Create Order")

symbol = st.text_input(
    "Trading Symbol",
    value="BTCUSDT"
)

side = st.selectbox(
    "Order Side",
    ["BUY", "SELL"]
)

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.001,
    value=0.001,
    step=0.001
)

price = None

if order_type == "LIMIT":

    price = st.number_input(
        "Limit Price",
        min_value=1.0,
        value=95000.0
    )

st.divider()

if st.button("Place Order"):

    try:

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        st.success("✅ Order placed successfully")

        st.subheader("Order Summary")

        st.json(response)

    except Exception as e:

        st.error(f"❌ {str(e)}")