import pyqrcode

qr = pyqrcode.create(input("Enter a text or link: "))

qr.png('qr.png', scale=10)