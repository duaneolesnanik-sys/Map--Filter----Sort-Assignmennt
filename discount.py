prices = [25.00, 50.00, 75.00, 100.00, 150.00]
discount_prices = list(map(lambda x: x*0.8, prices))
print("Original Prices: ",prices,"\nSale Prices: ",discount_prices)