import qrcode
import os
os.makedirs("generated_qr",exist_ok=True)

print("\nQR Code Generator\n")

data=input("Enter text or URL: ")
filename=input("Enter file name: ")

qr=qrcode.make(data)

path=f"generated_qr/{filename}.png"
qr.save(path)

print(f"\n✅ QR Code saved successfully")
print(f"📁 Location: {path}")