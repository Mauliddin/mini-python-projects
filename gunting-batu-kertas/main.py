import random
import os

score = [0,0]

def process(input):
    list_pilihan = ["Gunting","Batu","Kertas"]
    
    usr_input = list_pilihan[int(input)-1]
    com_input = random.choice(list_pilihan)
    
    if usr_input == com_input:
        hasil = "seri"
    elif usr_input == "Gunting":
        if com_input == "Batu":
            hasil = "Kalah"
        elif com_input == "Kertas":
            hasil = "Menang"
    elif usr_input == "Batu":
        if com_input == "Gunting":
            hasil = "Menang"
        elif com_input == "Kertas":
            hasil = "Kalah"
    elif usr_input == "Kertas":
        if com_input == "Gunting":
            hasil = "Kalah"
        elif com_input == "Batu":
            hasil = "Menang"
    
    if hasil == "Menang":
        score[0] = score[0] + 1
    elif hasil == "Kalah":
        score[1] = score[1] + 1
    
    print("\nPilihan Anda : "+usr_input)
    print("Pilihan Komputer : "+com_input)
    print("\nHasil : Anda "+hasil)
    print(f"\nscore : Anda ({score[0]}) : computer({score[1]})")
    
    os.system("pause")
    main()
    
    

def main():
    print("\nmasukkan pilihan:\n 1. Gunting\n 2. Batu\n 3. Kertas")
    pilihan = input("Pilihan : ")
    
    if (pilihan == "1" or  pilihan == "2" or pilihan == "3"):
        process(pilihan)
    else:
        print("\nPilihan anda salah: anda hanya dapat memilih salah satu angka dari 1 , 2 atau 3")
        os.system("pause")
        main()
main()