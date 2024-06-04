usr_input = input("Enter the word : ")
temp = usr_input[::-1]
if usr_input ==  temp:
    print(f"{usr_input} is palindrome")
else:
    print(f"{usr_input} is not palindrome")