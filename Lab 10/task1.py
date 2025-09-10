def discount(price, category):
    if category == "student":
        discount_rate = 0.9 if price > 1000 else 0.95
    else:
        discount_rate = 0.85 if price > 2000 else 1.0
    return price * discount_rate

print(discount(1000, "student"))