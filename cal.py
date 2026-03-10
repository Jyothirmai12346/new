import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
operation = sys.argv[3]

result = 0
if operation == "add":
    result = num1 + num2
elif operation == "sub":
    result = num1 - num2
elif operation == "mul":
    result = num1 * num2
else:
    print("Invalid operation")
    sys.exit()

print("Number1:", num1)
print("Number2:", num2)
print("Operation:", operation)
print("Result:", result)
