### Simple Calculator
# Can use addition, subtraction, multiplication and division

def add(x, y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

while True:

    symb = input("Please pick a maths operation to use:\n\
                    \tFor addition enter 'add'\n\
                    \tFor subtraction enter 'subtract'\n\
                    \tFor multiplication enter 'multiply'\n\
                    \tFor division enter 'divide':     ")

    ops = ['add', 'subtract', 'multiply', 'divide']

    if symb.lower() in ops:
        user_numb1 = float(input("Please enter a number: "))
        user_numb2 = float(input("Please enter another number: "))

        if symb.strip(' \'').lower() == 'add':
            result = add(user_numb1, user_numb2)
            print(f"{user_numb1} + {user_numb2} = {result}")
        elif symb.strip(' \'').lower() == 'subtract':
            result = subtract(user_numb1, user_numb2)
            print(f"{user_numb1} - {user_numb2} = {result}")
        elif symb.strip(' \'').lower() == 'multiply':
            result = multiply(user_numb1, user_numb2)
            print(f"{user_numb1} * {user_numb2} = {result}")
        elif symb.strip(' \'').lower() == 'divide':
            result = divide(user_numb1, user_numb2)
            print(f"{user_numb1} / {user_numb2} = {result}")
        break
    else:
        print("Invalid maths operator entered!")