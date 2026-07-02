import cv2

def read_qr():

    image_path=input("Enter QR image path: \n")

    image=cv2.imread(image_path)

    if image is None:
        print("Image not found.\n")
        return

    detector=cv2.QRCodeDetector()

    data,points,_=detector.detectAndDecode(image)

    if data:
        print("\nQR Code Found\n")

        print(data)
    else:
        print("No QR Code detected.")