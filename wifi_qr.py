import os
import qrcode

def generate_wifi_qr():

    ssid=input("Wi-Fi Name (SSID): ")
    password=input("Password: ")
    security=input("Security (WPA/WEP/None): ").upper()

    wifi_data=f"WIFI:T:{security};S:{ssid};P:{password};;"

    qr=qrcode.make(wifi_data)
    os.makedirs("generated_qr", exist_ok=True)

    filename=input("Filename: ")
    path=f"generated_qr/{filename}.png"

    qr.save(path)
    print("\nWi-Fi QR Created!")