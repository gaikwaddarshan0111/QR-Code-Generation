import qrcode
import uuid
import webbrowser
from datetime import datetime, UTC
import os

def generate_qr_code(amount):
    # Generate a unique transaction ID
    transaction_id = str(uuid.uuid4())  
    timestamp = datetime.now(UTC).isoformat()

    # Construct a payment payload (as string)
    data_str = (
        f"PAYMENT|TXN:{transaction_id}|AMOUNT:{amount}|"
        f"CURRENCY:INR|TIME:{timestamp}|PAYEE:merchant@example.com"
    )

    # Generate QR code
    qr = qrcode.make(data_str)

    # Save QR code
    qr_filename = f"payment_qr_{transaction_id[:8]}.png"
    qr.save(qr_filename)

    print(f"QR code saved as {qr_filename}")
    print(f"Transaction ID: {transaction_id}")

    # Open the QR code image in the default browser
    file_path = os.path.abspath(qr_filename)
    webbrowser.open(f"file://{file_path}")

if __name__ == "__main__":
    try:
        amount_input = float(input("Payment Amount: "))
        generate_qr_code(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
