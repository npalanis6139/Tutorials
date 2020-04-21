print("Welcome to my simple calculator")

while True:
    print("These are your options")
    print("Enter \"add\" to multiply two number together")
    print("Enter \"multiply\" to multiply two number together")
    print("Enter \"divide\" to multiply two number together")
    print("Enter \"subtract\" to multiply two number together")
    print("If you are done just type \"quit\"")
    user_input = input(":")

    if user_input == "quit":
        break

    elif user_input == "add":
        num1 = int(input("Enter the first number :"))
        num2 = int(input("Enter the second number"))
        result = int(num1 + num2)
        print(result)

    elif user_input == "multiply":
        num3 = input("Enter the first number :")
        num4 = input("Enter the second number")
        result = int(num3 * num4)
        print(result)

    elif user_input == "divide":
        num5 = input("Enter the first number :")
        num6 = input("Enter the second number")
        result = int(num5 / num6)
        print(result)

    elif user_input == "subtract":
        num7 = input("Enter the first number :")
        num8 = input("Enter the second number")
        result = int(num7 - num8)
        print(result)
