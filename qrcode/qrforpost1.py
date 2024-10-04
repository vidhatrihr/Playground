import qrcode
features = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
features.add_data('https://nptel.ac.in/courses/109/105/109105135/')
features.make(fit=True)
qr = features.make_image(fill='black', back_color='white')
qr.save('course1.png')
print("QR code generated and saved as 'qrcode.png'")
