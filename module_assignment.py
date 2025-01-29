QUESTION1
import random
a = random.randrange(100, 999, 5)
b = random.randrange(100, 999, 5)
c = random.randrange(100, 999, 5)
print(a)
print(b)
print(c)


QUESTION2
import random
lottery=[]
for i in range(100):
    lottery.append(random.randint(100000, 999999))
ans=random.sample(lottery,2)
print(ans)


QUESTION3
import random
otp=random.randint(100000,999999)
print(otp)


QUESTION4
import random
s=input("Enter string: ")
ch=random.choice(s)
print(ch)


QUESTION5
import random
import string
def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
print ("Random String is ", randomString(5) )


QUESTION6
import random
import string
def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print ("Password is ", randomPassword())



QUESTION7
import random
n1=random.uniform(1,100)
n2=random.uniform(1,100)
ans=n1*n2
print(f'multiplication of {n1} and {n2} random float numbers is{ans}')


QUESTION8
import secrets
print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))


QUESTION9
import random
dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))


QUESTION10
import random
from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 1, 1)

delta_days = (end_date - start_date).days
random_days = random.randint(0, delta_days)
random_date = start_date + timedelta(days=random_days)
print(f"Random date between {start_date.date()} and {end_date.date()} is {random_date.date()}")


