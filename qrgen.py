import pyqrcode
print("**** WELCOME TO FFREE QR GENERATOR BY TUSHAR GAUR *****")
text = input("Enter/Paste Text Or Url Here : ")
name = text
k = pyqrcode.create(name)
k.png('download.png', scale=10)
