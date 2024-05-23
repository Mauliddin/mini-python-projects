def check_input(text):
    usr_input = input(text)
    if usr_input.isnumeric():
        return int(usr_input)
    else:
        return check_input(text)

def main():
    total = 0
    number = check_input("Enter how many numbers : ")
    for i in range(number):
        total += check_input(f"Enter the {i+1} number : ")
    average = round(total/number,2)
    print(f"Average = {average}")
    
main()