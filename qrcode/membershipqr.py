import qrcode
features = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
features.add_data('https://linktr.ee/sanskritsociety_iitmbs')
features.make(fit=True)
qr = features.make_image(fill='black', back_color='white')
qr.save('linktree.png')
print("QR code generated and saved as 'qrcode.png'")
