import os
from classes import Antigensky
from PIL import Image, ImageDraw, ImageFont
from constants import (
    FINAL_NAME,
    FONT_PATH,
    FONT_SIZE,
    FONT_COLOR,
    BLUEPRINT_OFFSET,
    BLUEPRINT_PATH,
    REQUIRED_DIRS,
)


def collect_inputs_and_store_data() -> Antigensky:
    print("Provide values to be applied to your report")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    date_of_birth = input("Date of Birth: ")
    identification_number = input("Identification Number: ")
    sampling_date = input("Sampling Date: ")
    sampling_time = input("Sampling Time: ")
    sample_finished_time = input("Sample Finished Time: ")

    return Antigensky(
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        identification_number=identification_number,
        sampling_date=sampling_date,
        sampling_time=sampling_time,
        sample_finished_time=sample_finished_time,
    )


def draw_data_to_blueprint(antigensky: Antigensky, blueprint):
    print("Applying provided data...")

    full_name = f"{antigensky.first_name} {antigensky.last_name}"
    draw = ImageDraw.Draw(blueprint)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    draw.text((650, 2450), antigensky.sampling_date, FONT_COLOR, font=font)
    draw.text((2700, 2450), antigensky.sampling_time, FONT_COLOR, font=font)
    draw.text((3450, 2450), antigensky.sampling_date, FONT_COLOR, font=font)
    draw.text((4500, 2450), antigensky.sample_finished_time, FONT_COLOR, font=font)
    draw.text((2200, 3225), antigensky.identification_number, FONT_COLOR, font=font)
    draw.text((5800, 2900), antigensky.date_of_birth, FONT_COLOR, font=font)
    draw.text(
        (6500, 2425),
        full_name,
        FONT_COLOR,
        font=font,
    )


def generate_report(antigensky: Antigensky):
    print("Generating report...")

    blueprint = Image.open(BLUEPRINT_PATH, "r")
    qr = Image.open(antigensky.qr_path, "r")
    draw_data_to_blueprint(antigensky=antigensky, blueprint=blueprint)
    blueprint.paste(qr, BLUEPRINT_OFFSET)
    out_name = FINAL_NAME.format(antigensky.first_name, antigensky.last_name)
    blueprint.save(f"./results/{out_name}")

    print("Removing leftovers...")
    os.remove(antigensky.qr_path)


def init_dirs():
    for dir in REQUIRED_DIRS:
        if not os.path.isdir(dir):
            os.mkdir(dir)
