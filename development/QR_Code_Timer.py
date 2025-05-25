import qrcode
import uuid
from datetime import datetime, UTC
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

remaining_seconds = 0
timer_job = None
your_upi_id = "gaikwaddarshan0111-1@okicici"

# Store transaction IDs internally
transaction_log = []

def update_timer():
    global remaining_seconds, timer_job
    if remaining_seconds > 0:
        mins , secs = divmod(remaining_seconds,60)
        timer_label.config(text=f"QR Code expires in : {mins:02d}:{secs:02d}")
        remaining_seconds -= 1
        timer_job = root.after(1000, update_timer)
    else:
        timer_label.config(text="QR Code Is Expired")
        
def generate_qr_code(amount):
    global remaining_seconds, timer_job
    
    # Cancel any existing timer
    if timer_job:
        root.after_cancel(timer_job)
    
    transaction_id = str(uuid.uuid4())  
    timestamp = datetime.now(UTC).isoformat()

    ##data_str = (
     ##   f"PAYMENT|TXN:{transaction_id}|AMOUNT:{amount}|"
     ##   f"CURRENCY:INR|TIME:{timestamp}|PAYEE:merchant@example.com"
    ##)
    data_str = (
        f"upi://pay?pa={your_upi_id}&pn=Darshan Gaikwad&am={amount}&cu=INR&tn=Payment%20for%20Order%20{transaction_id}"
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
    
    #start 2 minutes timer for payment
    remaining_seconds = 2 * 60
    update_timer()
    
    # Schedule expiration
    root.after(2 * 60 * 1000,expire_qr_code)
    

        
def expire_qr_code():
    global timer_job
    if timer_job:
        root.after_cancel(timer_job)
    timer_label.config(text="")    
    qr_label.config(image ="")
    qr_label.image = None
    verified_label.config(text="⚠️  QR Code is expired", fg="red")
    transaction_id_var.set("")

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
entry = tk.Entry(root, width=10)
entry.pack(pady=5)

submit_btn = tk.Button(root, text="Generate QR Code", command=on_submit)
submit_btn.pack(pady=10)

# Label for verified checkmark
verified_label = tk.Label(root, text="")
verified_label.pack()

#label for countdown timer 
timer_label = tk.Label(root, text="",font=("Arial",12))
timer_label.pack()


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