import qrcode

search = input("Enter the website you want barcode for:\n")
data = search
img = qrcode.make(data)
name = input("how do you want to call it?\n")
img.save(name + ".png")





