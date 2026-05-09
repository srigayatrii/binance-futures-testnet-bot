from bot.client import client

try:

    balance = client.futures_account_balance()

    print(balance)

except Exception as e:

    print(e)