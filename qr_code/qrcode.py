# import qrcode

# # Define the data to be encoded in the QR code
# data = "https://www.example.com/"

# # Create a QRCode object
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )

# # Add data to the QRCode object
# qr.add_data(data)
# qr.make(fit=True)

# # Create an image from the QRCode object
# img = qr.make_image(fill_color="black", back_color="white")

# # Save the image to a file
# img.save("qr_code.png")

# # Display the QR code image
# img.show()
