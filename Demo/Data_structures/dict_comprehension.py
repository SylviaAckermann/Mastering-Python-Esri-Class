
# Write set to dictionary
currencies = [
    {"bitcoin", "BTC"},
    {"litecoin", "LTC"},
    {"ethereum", "ETH"},
]

currency_dict = {}
for currency_name, currency_symbol in currencies:
    currency_dict[currency_symbol] = currency_name

print(currency_dict)

currency_dict = {name: symbol for name, symbol in currencies}
print(currency_dict)