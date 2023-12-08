from qrcode import QRCode
from PIL import Image

# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Qr(url):
    qr = QRCode(version=1, box_size=30, border=2)
    qr.add_data(url)
    qr.make(True)
    img = qr.make_image(fill_color="black", back_color="white")
    logo = Image.open("menu (1).png")
    logo = logo.resize((150, 150))
    img_w, img_h = img.size
    logo_w, logo_h = logo.size
    pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
    img.paste(logo, pos)
    img.save("qr_code__.png")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Qr('https://iliass2.github.io/menu-2/')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
