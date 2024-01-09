import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=8,
)
qr.add_data("https://github.com/arshi1606")
qr.make(fit=True)

img = qr.make_image(fill_color="Yellow", back_color="black")

img.save("Arshi_GitHUB.png")
