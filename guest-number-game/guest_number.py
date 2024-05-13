from random import randint

number = randint(1,100)
chance = 10

while True:
    usr_input = input("\nEnter Number (1-100) : ")
    if usr_input.isnumeric():
        
        usr_input = int(usr_input)
        if usr_input == number:
            print("=== YOU ARE RIGHT ===")
            break
        elif usr_input > number:
            print(" === TO HIGH ===")
        elif usr_input < number:
            print(" === TO LOW ===")
        
        if chance == 0:
            print("Your chance to guess is over")
            break
        else:
            print(f"Your only have {chance} to guess")
            chance = chance - 1
        
        