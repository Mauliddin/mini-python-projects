import qrcode
import cv2

def usr_input_check():
    usr_input = input("Enter the choice : ")
    if usr_input == "1" or usr_input == "2":
        return usr_input
    else:
        return usr_input_check()
    
def create_qr(data, file):
    img = qrcode.make(data)
    img.save(file)
    img.show()

def read_qr(file):
    img = cv2.imread(file)
    det = cv2.QRCodeDetector()
    data, _ , _ = det.detectAndDecode(img)
    return data

def main():
    print("1. Make QR Code \n2. Read QR Code")
    choice = usr_input_check()
    if choice == "1":
        url = input("Enter the URl: ")
        path = input("Enter the path and filename : ")
        create_qr(url,path)
    elif choice == "2":
        path = input("Enter the path QR-Code: ")
        url = read_qr(path)
        print(f"The URL : {url}")
main()