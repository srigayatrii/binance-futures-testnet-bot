from bot.logging_config import logger
import random


def place_order(symbol, side, order_type, quantity, price=None):

    logger.info(
        f"Received order request: "
        f"{side} {quantity} {symbol} "
        f"as {order_type}"
    )

    try:

        mock_response = {
            "orderId": random.randint(10000, 99999),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price,
            "status": "FILLED"
        }

        logger.info(
            f"Order successful: {mock_response}"
        )

        return mock_response

    except Exception as e:

        logger.error(
            f"Order failed: {str(e)}"
        )

        raise