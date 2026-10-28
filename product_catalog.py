def calculate_total_price(price, quantity):
    total_price = price * quantity
    return total_price


price = 1500

quantity = 3

total = calculate_total_price(price, quantity)

print(total)
