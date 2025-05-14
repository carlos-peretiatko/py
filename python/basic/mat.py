x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

operation = input("Enter an operation (+, -, *, /):")

match operation:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "*":
        print(x * y)
    case "/":
        print(x / y)
    case _:
        print("Invalid operation")
    