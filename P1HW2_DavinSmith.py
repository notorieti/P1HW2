# Davin Smith
# 2-16-25
# Assignment Name: P1HW2
# Create a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses")
budget=int(input("Enter budget:"))
print()
location= str(input("Enter your travel destination:"))
print()
gas= int(input("How much do you think you will spend on gas?:"))
print()
lodging= int(input("Approximately, how much will you need for accomodation/hotel?:"))
print()
food= int(input("Last, how much do you need for food?:"))
print()

print("-"*12,"Travel Expenses","-"*12)
print("Location:", location)

# calculation
balance=budget-(gas + lodging + food)
print("Remaining Balance:", balance)
print("Remaining Balance:", budget-(gas + lodging + food))


#Pseudocode
##Ask User to enter their budget.
##Ask user to enter travel destination.
##Ask user for amount they will spend on gas.
##Ask user for amount they will spend on accomodation
##Ask user for amount they will spend on food
##Add expenses
##Subtract expense from budget
##Display Results
