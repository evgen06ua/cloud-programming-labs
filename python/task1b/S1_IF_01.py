def shipping_cost(weight, member):
    if not isinstance(weight, (int, float)) or weight <= 0:
        return None
    
    if weight <= 1:
        cost = 10
    elif weight <= 5:
        cost = 20
    else:
        cost = 30
    
    if member:
        cost = cost * 0.8
    
    return cost

print(shipping_cost(0.5, False))
print(shipping_cost(1, False))
print(shipping_cost(3, False))
print(shipping_cost(3, True))
print(shipping_cost(10, False))
print(shipping_cost(-1, False))
