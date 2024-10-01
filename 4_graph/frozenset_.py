stock_prices = {
    frozenset(["APPLE", "GOOGLE"]): 100,
    frozenset(["MICROSOFT", "FACEBOOK"]): 80
}
apple_google_price = stock_prices[frozenset(["GOOGLE","APPLE"])]
print(apple_google_price)  # Output: 100

microsoft_facebook_price = stock_prices[frozenset(["MICROSOFT", "FACEBOOK"])]
print(microsoft_facebook_price)  # Output: 80