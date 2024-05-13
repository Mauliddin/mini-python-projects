import math

def convert(radiant):
    return radiant * (180/math.pi)


def main():
    usr_input = input("Enter Radiant : ")
    if usr_input.isnumeric():
        in_degree = convert(int(usr_input))
        print(f"{usr_input} Radiant = {round(in_degree, 2)} degree")

main()
