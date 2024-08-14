# import qrcode

# image = qrcode.make("https://www.youtube.com/")
# image.save('youtube.png')

import qrcode

# Data to encode
data = "https://www.youtube.com/"

# Generate QR code
img = qrcode.make(data)

# Save the image
img.save('youtube.png')
