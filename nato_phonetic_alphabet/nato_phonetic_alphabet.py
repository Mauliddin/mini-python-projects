import pandas
def generate_phonetic():
    word = input("Enter the Word : ").upper()
    try:
        all_word = [phonetic[t] for t in word]
    except KeyError:
        print("Only Enter Letter !")
        generate_phonetic()
    else:
        print(all_word)
        
path = "nato_phonetic_alphabet/nato_phonetic_alphabet.csv"
data = pandas.read_csv(path)
#phonetic = data.to_dict(index=False, orient="split")["data"]
phonetic = {row.letter:row.code for (index, row) in data.iterrows()}
generate_phonetic()