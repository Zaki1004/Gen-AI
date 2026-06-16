from pathlib import Path
import qrcode

BASE_DIR = Path(__file__).resolve().parent.parent

QR_DIR = (
    BASE_DIR /
    "assets" /
    "qrcode"
)

QR_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def generate_qr(order_number):

    qr_data = f"PAYMENT-{order_number}"

    qr = qrcode.make(qr_data)

    file_name = (
        f"{order_number}.png"
    )

    file_path = (
        QR_DIR /
        file_name
    )

    qr.save(file_path)

    return str(file_path)