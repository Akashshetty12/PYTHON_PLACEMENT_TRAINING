import qrcode
a = qrcode.QRCode()
a.add_data("https://github.com/Akashshetty12")
a.make(fit=True)
img = a.make_image()
img.save("qrcode.png")