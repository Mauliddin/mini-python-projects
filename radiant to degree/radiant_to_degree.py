def convert(radiant):
  return radiant * (180/3.14)

def main():
  usr_input = input("Enter Radiant : ")
  if usr_input.isnumeric():
    print(f"{usr_input} Radiant = {convert(int(usr_input)} degree")

if __name__ == "__main__":
  main()
