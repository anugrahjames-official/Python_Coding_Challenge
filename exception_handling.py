num2 = 0

try:
    num1 = 10 / num2
    print(num1)
    print("Try block completed.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

print("Program completed.")