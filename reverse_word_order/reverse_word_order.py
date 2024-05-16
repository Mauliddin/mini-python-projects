def reverse(word):
    return " ".join(word.split(" ")[::-1])

def main():
    words = str(input("Enter The word : "))
    print(reverse(words))
    
main()