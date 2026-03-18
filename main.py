print("-----")

# User's numbers inserted

prompt_one = input("Please enter the first number: ")
user_response_one = float(prompt_one)
prompt_two = input("Please enter the second number: ")
user_response_two = float(prompt_two)

# Symbols to choose

print("-----")
print("Please choose the symbol from the list below:")
print("-----")
print("+\n-\n*\n/\n%")
print("-----")

# The action of choosing

prompt_three = input("Your symbol: ")
print("-----")

# if (condition) => result

if prompt_three == '+':
    print('Result =', user_response_one + user_response_two)
elif prompt_three == '-':
    print('Result =', user_response_one - user_response_two)
elif prompt_three == '*':
    print('Result =', user_response_one * user_response_two)
elif prompt_three == '/':
    print('Result =', user_response_one / user_response_two)
elif prompt_three == '%':
    print('Result =', (user_response_one / 100) * user_response_two)
print("-----")
