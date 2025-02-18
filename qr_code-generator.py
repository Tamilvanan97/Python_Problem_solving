import qrcode

data = input('Enter an URL or Text: ').strip()
filename = input('Enter a file name: ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make()
image = qr.make_image(fill_color ='black', back_color = 'white')
image.save(filename)
print('QR code saved as ',filename)