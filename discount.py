# While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10.
#  If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.


def fun(quantity,price):
    if(quantity>=10):
        a=quantity*price
        dis=a*(10/100)
        ans=a-dis
        print("After 10% discount price is:",ans)
    else:
        print("discount is not offered and price is:",price)
quantity=int(input("Enter number of quantity:"))
price=float(input("Enter the price:"))
fun(quantity,price)


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

