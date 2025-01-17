


#Question1:
class Demo:
    value=10
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def Fun(self):
        return self.first_name
    def Gun(self):
        return self.last_name
obj1=Demo("ganga","senamsetti")
obj2=Demo("malika","chipurupalli")
print(obj1.Fun())
print(obj1.Gun())
print(obj2.Fun())
print(obj2.Gun())





#Question2:
class BookStore:
    NoofBooks=0
    def __init__(self,name,author):
        self.name=name
        self.author=author
        BookStore.NoofBooks+=1
    def Display(self):
        print(self.name+" by "+self.author+". "+"No.of books"+str(BookStore.NoofBooks))

Obj1=BookStore("Linux Programming","robert love")
Obj1.Display()  
Obj2=BookStore("C Programming","Dennis Ritches")
Obj2.Display()




#Question3
class Circle:
    PI=3.14
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0
        
    def Accept(self):
        self.radius=float(input("Enter the radius:"))
        
    def calculateArea(self):
        area=Circle.PI*self.radius*self.radius
        return area
    
    def cal_circumference(self):
        circumference=2*Circle.PI*self.radius
        return circumference
        
    def display(self):
        
        print("Area of circle:"+str(self.calculateArea()))
        print("circumference of circle:"+str(self.cal_circumference()))

obj1=Circle()
obj1.Accept()
obj1.display()




#Question4
class BankAccount:
    ROI=10.5
    def __init__(self):
        self.name=input("Enter name:")
        self.amount=float(input("Anter amount: "))
    
    def deposit(self):
        amo=float(input("enter amount to deposit:"))
        self.amount+=amo
        
    
    def withdraw(self):
        amo=float(input("enter amount to withdraw:"))
        self.amount-=amo
        
    def cal_Interest(self):
        
        self.amount+=(self.amount*BankAccount.ROI)/100
        print("calculated interest: "+str(self.amount))
    
    def display(self):
        print("Name:"+self.name)
        print("Amount in account:"+str(self.amount))

b=BankAccount()
b.deposit()
b.display()
b.withdraw()
b.display()
b.cal_Interest()
b.display()




#Question5
class Numbers:
    def __init__(self):
        self.value=int(input("Enter the number: "))
        
    def ChkPrime(self):
        if self.value<=1:
            return 0
        for i in range(2,self.value):
            if self.value%i==0:
                return 0
        return 1
    
    def ChkPerfect(self):
        if self.value<=1:
            return False
        s=0
        for i in range(1,self.value):
            if self.value%i==0:
                s+=i
                
        return s==self.value
    
    def find_factors(self):
        factors = []
        for i in range(1, self.value+1):
            if self.value % i == 0:
                factors.append(i)
        return factors
    
    def SumFactors(self):
        
        s=0
        for i in range(1, self.value+1):
            if self.value % i == 0:
                s+=self.value
        return s

n=Numbers()
print(n.ChkPrime())
print(n.ChkPerfect())
print(n.find_factors())
print(n.SumFactors())
        



#Question 6
class Numbers:
    def __init__(self):
        self.value1=0
        self.value2=0
        
    def Accept(self):
        self.value1=int(input("Enter value1: "))
        self.value2=int(input("Enter value2: "))
    
    def Addition(self):
        result=self.value1+self.value2
        print(result)
    
    def Subtraction(self):
        result=self.value1-self.value2
        print(result)
    
    def Multiplication(self):
        result=self.value1*self.value2
        print(result)
    
    def Division(self):
        result=self.value1/self.value2
        print(result)
    
obj1=Numbers()
obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()
        
      