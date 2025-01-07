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
