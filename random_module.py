import random
lucky=int(input("enter your lucky number: "))
if lucky>1 and lucky<100:
    while True:
        n=random.randint(1,100)
        print("Genrerated random num is:",n)
        if n==lucky:
            print("Your lucky number matched random number")
            break
else:
    print("please enter random number between 1 to 100")