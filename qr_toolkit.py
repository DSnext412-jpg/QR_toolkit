from generator import generate_qr
from reader import read_qr
from wifi_qr import generate_wifi_qr
from logo_qr import generate_logo_qr

def menu():
    while True:
        print("\n==============================")
        print("      QR CODE TOOLKIT")
        print("==============================")
        print("1. Generate QR Code")
        print("2. Read QR Code")
        print("3. Generate Wi-Fi QR")
        print("4. Generate Logo QR")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            generate_qr()
        elif choice == "2":
            read_qr()
        elif choice == "3":
            generate_wifi_qr()
        elif choice == "4":
            generate_logo_qr()
        elif choice == "5":
            print("Thank you for using QR Toolkit.")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    menu()