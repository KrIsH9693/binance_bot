# bot.py

from binance.client import Client
from binance.enums import *
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
        logging.info("Binance Futures Testnet client initialized")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            print(f"Placing {order_type} order: {symbol} {side} {quantity} @ {price}")
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=SIDE_BUY if side == 'BUY' else SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            else:
                logging.error("Unsupported order type: %s", order_type)
                return None

            print("Order response:", order)
            logging.info("Order placed: %s", order)
            return order
        except Exception as e:
            print("❌ Error placing order:", e)
            logging.error("Error placing order: %s", e)
            return None
