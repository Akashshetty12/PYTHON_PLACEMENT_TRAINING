import qrcode

a = qrcode.QRCode()
# a.add_data("This is Python")
a.add_data("https://github.com/Akashshetty12")
a.make(fit=True)
img = a.make_image()
img.save("qrcode.png")

# def nitte(n):
#     c = 0
#     if (n <= 1):
#         return
#     for i in range(n):
#         nitte(i)
#         print("hai")
#         c = c+2
#     print(c)
# b = nitte(3)
# print(b)