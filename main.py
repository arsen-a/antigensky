import qrcode
import uuid
import os
from PIL import Image, ImageDraw, ImageFont

BLUEPRINT_PATH = "./assets/blueprint.png"
BLUEPRINT_OFFSET = (700, 8300)
BOX_SIZE = 30
BORDER = 0
FONT_SIZE = 180
FONT_COLOR = (0, 0, 0)


class Antigensky:
    def __init__(self, first_name, last_name, date_of_birth, sampling_date):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sampling_date = sampling_date
        self.qr_data = f"(1)First name: {self.first_name}(2)Last name: {self.last_name}(3)SARS-CoV-2  Ag (nazofarinks), brzi test: Result: NEGATIVAN(4)Sampling date: {self.sampling_date}(5)Sampling time: 14:42"
        self.qr_path = None

    def generate_qr(self):
        self.qr_path = f"./assets/qrs/{self.id}.png"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=BOX_SIZE,
            border=BORDER,
        )

        qr.add_data(self.qr_data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save(self.qr_path)


def collect_inputs_and_store_data():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    date_of_birth = input("Date of Birth: ")
    sampling_date = input("Sampling Date: ")

    return Antigensky(
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        sampling_date=sampling_date,
    )


def main():
    antigensky = collect_inputs_and_store_data()
    antigensky.generate_qr()

    blueprint = Image.open(BLUEPRINT_PATH, "r")
    qr = Image.open(antigensky.qr_path, "r")

    draw = ImageDraw.Draw(blueprint)
    font = ImageFont.truetype("./assets/default-font.ttf", FONT_SIZE)

    draw.text((650, 2450), antigensky.sampling_date, FONT_COLOR, font=font)
    draw.text(
        (6500, 2450),
        f"{antigensky.first_name} {antigensky.last_name}",
        FONT_COLOR,
        font=font,
    )

    blueprint.paste(qr, BLUEPRINT_OFFSET)
    blueprint.save("final.png")
    os.remove(antigensky.qr_path)


if __name__ == "__main__":
    main()
