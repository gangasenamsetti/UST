#QUESTION1
import os

# Replace 'Downloads' with the path to your downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# List the contents of the folder
contents = os.listdir(downloads_folder)

# Iterate through the items and check if each is a file or folder
for item in contents:
    item_path = os.path.join(downloads_folder, item)
    if os.path.isfile(item_path):
        print(f"{item} - File")
    elif os.path.isdir(item_path):
        print(f"{item} - Folder")
    else:
        print(f"{item} - Unknown")




#QUESTION 2
import string

# Print all ASCII letters
print(string.ascii_letters)



#QUESTION 3
from random import sample
from string import ascii_letters

# Randomly sample 5 letters
five_letters = ''.join(sample(ascii_letters, 5))

print(five_letters)



#QUESTION 4
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# a. Take input from the user and format the date
date_input = input("Enter a date (dd/mm/yyyy): ")
input_date = datetime.strptime(date_input, "%d/%m/%Y")
formatted_date = input_date.strftime("%A %d %B %Y")
print("Formatted Date:", formatted_date)

# b. Print the day of the week
day_of_week = input_date.strftime("%A")
print("Day of the week:", day_of_week)

# c. Add 15 days and 23 hours to the input date
new_date = input_date + timedelta(days=15, hours=23)
print("Date after adding 15 days and 23 hours:", new_date.strftime("%A %d %B %Y %H:%M"))

# d. Calculate the date 6 months from the current date
current_date = datetime.now()
date_6_months = current_date + relativedelta(months=6)
print("Date 6 months from today:", date_6_months.strftime("%A %d %B %Y"))




#QUESTION 5
import random

# Options for the game
options = ["rock", "paper", "scissors"]

# Get user input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Get computer's choice
computer_choice = random.choice(options)

# Print choices
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("Computer wins!")

    