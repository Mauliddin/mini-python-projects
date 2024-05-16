
def remove_duplicate(l_list: list):
    return list(set(l_list))

def main():
    name = ["Jack", "Maria", "Jack", "Diana", "Rose", "Rose"]
    print(f"before : {name}")
    print(f"after : {remove_duplicate(name)}")

main()