# main.py

from config import API_KEY, API_SECRET
from bot import BasicBot
from utils import setup_logger

def get_user_input():
    print("=== Binance Futures Trading Bot ===")
    symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper()
    side = input("Order Side (BUY or SELL): ").upper()
    order_type = input("Order Type (MARKET or LIMIT): ").upper()
    quantity = float(input("Quantity: "))
    price = None
    if order_type == 'LIMIT':
        price = float(input("Enter Limit Price: "))  # ✅ FIXED: price as float
    return symbol, side, order_type, quantity, price

def main():
    setup_logger()
    bot = BasicBot(API_KEY, API_SECRET)

    symbol, side, order_type, quantity, price = get_user_input()
    result = bot.place_order(symbol, side, order_type, quantity, price)

    if result:
        print("✅ Order placed successfully!")
        print(result)
    else:
        print("❌ Order failed. Check bot.log for details.")

if __name__ == "__main__":
    main()
