# install library
# create a function that collects a text and convers it to a qr code
# save the qr code as image
import qrcode

def generate_qrCode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save("qrimage.png")

text = input("Enter the data you want in Qr code: ")
generate_qrCode(text)