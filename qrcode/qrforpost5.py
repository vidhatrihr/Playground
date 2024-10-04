import qrcode
features = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
features.add_data('https://nptel.ac.in/courses/109101195')
features.make(fit=True)
qr = features.make_image(fill='black', back_color='white')
qr.save('course4.png')
print("QR code generated and saved as 'qrcode.png'")
