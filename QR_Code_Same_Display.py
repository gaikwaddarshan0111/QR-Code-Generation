import qrcode
import uuid
from datetime import datetime, UTC
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

# Store transaction IDs internally
transaction_log = []

def generate_qr_code(amount):
    transaction_id = str(uuid.uuid4())  
    timestamp = datetime.now(UTC).isoformat()

    data_str = (
        f"PAYMENT|TXN:{transaction_id}|AMOUNT:{amount}|"
        f"CURRENCY:INR|TIME:{timestamp}|PAYEE:merchant@example.com"
    )

    # Generate QR code
    qr_img = qrcode.make(data_str)

    # Convert QR to ImageTk for display
    buffer = io.BytesIO()
    qr_img.save(buffer, format="PNG")
    buffer.seek(0)
    img = Image.open(buffer)
    img = img.resize((250, 250))  # Resize if needed
    tk_img = ImageTk.PhotoImage(img)

    # Display in UI
    qr_label.config(image=tk_img)
    qr_label.image = tk_img  # Keep reference to avoid garbage collection

    # Update transaction ID in text box
    transaction_id_var.set(transaction_id)

    # Show verified checkmark
    verified_label.config(text="✅ Payment QR Generated", fg="blue")

    # Save transaction ID internally
    transaction_log.append(transaction_id)

def on_submit():
    try:
        amount = float(entry.get())
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        generate_qr_code(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for the amount.")

# UI Setup
root = tk.Tk()
root.title("Payment QR Code Generator")

tk.Label(root, text="Enter Payment Amount (INR):").pack(pady=10)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

submit_btn = tk.Button(root, text="Generate QR Code", command=on_submit)
submit_btn.pack(pady=10)

# Label for verified checkmark
verified_label = tk.Label(root, text="")
verified_label.pack()

# Entry for displaying transaction ID
# Frame for centering
txn_frame = tk.Frame(root)
txn_frame.pack(pady=(10, 0))

# Label inside frame
tk.Label(txn_frame, text="Transaction ID:").pack()

# Entry inside frame
transaction_id_var = tk.StringVar()
txn_id_entry = tk.Entry(txn_frame, textvariable=transaction_id_var, width=50, state='readonly', justify='center')
txn_id_entry.pack(pady=5)

# Label for displaying QR code
qr_label = tk.Label(root)
qr_label.pack(pady=20)

root.mainloop()
