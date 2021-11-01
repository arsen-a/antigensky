import qrcode
import uuid
from constants import BOX_SIZE, BORDER


class Antigensky:
    def __init__(
        self,
        first_name,
        last_name,
        date_of_birth,
        identification_number,
        sampling_date,
        sampling_time,
        sample_finished_time,
    ):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.identification_number = identification_number
        self.sampling_date = sampling_date
        self.sampling_time = sampling_time
        self.sample_finished_time = sample_finished_time

        self.qr_data = f"(1)First name: {self.first_name}(2)Last name: {self.last_name}(3)SARS-CoV-2  Ag (nazofarinks), brzi test: Result: NEGATIVAN(4)Sampling date: {self.sampling_date}(5)Sampling time: {self.sampling_time}"
        self.qr_path = None

    def generate_qr(self):
        print("Generating QR code...")

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
