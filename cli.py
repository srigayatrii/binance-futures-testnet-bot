import typer
from rich import print
from rich.pretty import pprint

from bot.orders import place_order

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

app = typer.Typer()


@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = typer.Option(None)
):

    try:

        side = side.upper()
        order_type = order_type.upper()

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

        print("\n[bold green]✅ Order Successful[/bold green]\n")
        pprint(response)

    except Exception as e:

        print(f"\n[bold red]❌ Error:[/bold red] {e}")


if __name__ == "__main__":
    app()