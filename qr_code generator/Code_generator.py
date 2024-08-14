import qrcode         # pip install qrcode[pil]

# Data to encode
data = "https://www.youtube.com/"

# Generate QR code
img = qrcode.make(data)

# Save the image
img.save('youtube.png')
