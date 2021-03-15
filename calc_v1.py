### Simple Calculator
# Can use addition, subtraction, multiplication and division

user_numb1 = float(input("Please enter another number: "))
user_symb = input("Please pick a maths operation to use:\n\
    \tFor addition enter '+'\n\
    \tFor subtraction enter '-'\n\
    \tFor multiplication enter '*'\n\
    \tFor division enter '\\': ")
user_numb2 = float(input("Please enter another number: "))

if user_symb.strip('\'') == '+':
    result = user_numb1 + user_numb2
    print(f"The result of {user_numb1} + {user_numb2} = {result}")
elif user_symb.strip('\'') == '-':
    result = user_numb1 - user_numb2
    print(f"The result of {user_numb1} - {user_numb2} = {result}")
elif user_symb.strip('\'') == '*':
    result = user_numb1 * user_numb2
    print(f"The result of {user_numb1} * {user_numb2} = {result}")
else:
    result = user_numb1 / user_numb2
    print(f"The result of {user_numb1} / {user_numb2} = {result}")