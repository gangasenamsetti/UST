items=['Bread','Cookies','Butter','Cheese','Yogurt']
prices=[40,80,120,180,60]
print(items)
cart=[]
while True:
    print("What do you want to do?")
    print("1: Enter 1 for viewing the items")
    print("2: Enter 2 for adding the items in the cart")
    print("3: Enter 3 for updating the items in cart")
    print("4: Enter 4 for deleting the items in cart")
    print("5: Enter 5 for printing the bill")
    print("6: Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            print("Name:", item, "Price:", price)
    elif choice==2:
        item_name = input("Enter the item name: ")
        if item_name in items:
            quantity = int(input("Enter the quantity: "))
            price = prices[items.index(item_name)]
            cart.append([item_name, quantity, price])
        else:
            print("Item not found")
    elif choice==3:
        item_name = input("Which item to be updated: ")
        for item in cart:
            if item[0] == item_name:
                new_quantity = int(input("Enter the quantity to be updated: "))
                item[1] = new_quantity
                break
        else:
            print("Item not found in cart.")
    elif choice == 4:
        item_name = input("Which item to be removed: ")
        for item in cart:
            if item[0] == item_name:
                cart.remove(item)
            else:
                print("Item not found in cart")
    elif choice==5:
        total_amount = 0
        for item in cart:
            name, quantity, price = item
            total = quantity * price
            total_amount += total
            print(f"{name},{quantity},{price},{total}")
        print("Total Amount of Bill:", total_amount)
    elif choice==6:
        print("Exit")
    else:
        print("Invalid input")