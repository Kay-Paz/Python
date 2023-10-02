# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

# Desired Output:
# Invalid input
# Maximum is 10
# Minimum is 2

largest = 0
smallest = None
intNum = 0

numList = []

while True:
    num = input("Enter a number: ")
    if num == 'done':
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break
    try:
        intNum = int(num)
        numList.append(intNum)
        if smallest is None:
            smallest = intNum
        elif intNum < smallest:
            smallest = intNum
        if intNum > largest:
            largest = intNum
    except:
        print('Invalid input')
        continue

