from bot.logging_config import logger
from bot.client import client


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        # LIMIT order needs extra params
        if order_type == "LIMIT":

            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Sending order: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Order successful: {response}")

        return response

    except Exception as e:

        logger.error(f"Order failed: {str(e)}")

        raise