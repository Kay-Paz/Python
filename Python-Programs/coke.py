# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.


balance = 50

while balance > 0:
    print("Amount Due:", balance)
    deposit = int(input("Insert Coin:"))
    if deposit in [25, 10, 5]:
        balance -= deposit

change_owed = abs(balance)
print("Change Owed:", change_owed)