laptop_brand = "Hewlett Parkard"
exchange_rate = 131.123456
price_in_usd = 1080
message = 'The price of this %s laptop is %d kshs and the exchange rate is 1 usd for %.2f kshs' %(laptop_brand, (price_in_usd*exchange_rate), exchange_rate)
print(message)