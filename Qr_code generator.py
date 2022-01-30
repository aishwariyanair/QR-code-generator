import qrcode
import datetime

qr1=qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=3
)

x=datetime.datetime.now()

qr1.add_data("Hello...u have successfully scanned the QR code at "+str(x))
img=qr1.make_image(fill_color="blue",back_color="black")
img.save("First Qr.png")