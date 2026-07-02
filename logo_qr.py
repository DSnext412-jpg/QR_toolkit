import os
import qrcode
from PIL import Image

def generate_logo_qr():

    data=input("Enter URL/Text: ")

    filename=input("Filename: ")

    logo_path="assets/logo.png"

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    qr.add_data(data)

    qr.make(fit=True)

    img=qr.make_image(
        fill_color="black",
        back_color="white"
    ).convert("RGB")

    if not os.path.exists(logo_path):
        print("❌ assets/logo.png not found.")
        return

    logo=Image.open(logo_path)

    qr_width,qr_height=img.size

    logo_size=qr_width//4

    logo=logo.resize((logo_size, logo_size))

    x=(qr_width - logo_size)//2
    y=(qr_height - logo_size)//2

    img.paste(logo,(x, y), mask=logo if logo.mode == "RGBA" else None)

    os.makedirs("generated_qr", exist_ok=True)

    path=f"generated_qr/{filename}.png"

    img.save(path)

    print("Logo QR Generated!")