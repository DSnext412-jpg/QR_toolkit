import os
import qrcode


def generate_qr():
    os.makedirs("generated_qr",exist_ok=True)

    data=input("Enter text or URL: ")
    filename=input("Enter filename: ")

    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img=qr.make_image(
        fill_color="black",
        back_color="white"
    )

    path=f"generated_qr/{filename}.png"
    img.save(path)

    print(f"\nQR Code saved successfully!")
    print(f"{path}")