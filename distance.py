# Receive the following arguments from the user:
# Kilometers to drive
# Liters-per-kilometer usage of the car
# Price per liter of fuel
# Calculate the cost of the trip and display it to the user in the console


def cost(km,liters,price):
    tot_lit=km*liters
    return tot_lit*price

km=float(input())
liters=float(input())
price=float(input())
print("Total cost :",cost(km,liters,price))
