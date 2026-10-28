products = [ 
    {"name": "Keyboard", "price": 45}, 
    {"name": "Monitor", "price": 180}, 
    {"name": "Mouse", "price": 25}, 
    {"name": "Headphones", "price": 75}, 
    {"name": "USB Drive", "price": 15}, 
    {"name": "Webcam", "price": 60} 
] 
under_50 = list(filter(lambda x: x["price"] < 50, products))
print("Products under $50:")
for item in under_50:
    print(f"{item["name"]} - ${item["price"]}")