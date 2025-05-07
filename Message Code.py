import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # For Gmail
SMTP_PORT = 465
ADMIN_EMAIL = "giftanthony.job@gmail.com"
EMAIL_PASSWORD = "zjei whgc jmzm zrjo"  # Replace with actual app password


def ask_to_send_email():
    # Ask if the customer wants to send an email
    response = messagebox.askyesno("Send Email", "Do you want to send us an email?")
    if response:
        ask_for_name()
    else:
        messagebox.showinfo("Thank You", "No problem! Feel free to reach out to us anytime.")
        root.destroy()


def ask_for_name():
    # Create a new window for name input
    name_window = tk.Toplevel(root)
    name_window.title("Enter Your Name")
    name_window.geometry("300x100")

    tk.Label(name_window, text="Please enter your name:").pack(pady=10)
    name_entry = tk.Entry(name_window)
    name_entry.pack(pady=5)

    def submit_name():
        name = name_entry.get().strip()
        if name:
            name_window.destroy()
            ask_for_email(name)
        else:
            messagebox.showwarning("Invalid Input", "Name cannot be empty. Please try again.")

    tk.Button(name_window, text="OK", command=submit_name).pack(pady=5)


def ask_for_email(name):
    # Create a new window for email input
    email_window = tk.Toplevel(root)
    email_window.title("Enter Your Email")
    email_window.geometry("300x100")

    tk.Label(email_window, text="Please enter your email address:").pack(pady=10)
    email_entry = tk.Entry(email_window)
    email_entry.pack(pady=5)

    def submit_email():
        email = email_entry.get().strip()
        if email:
            email_window.destroy()
            ask_for_message(name, email)
        else:
            messagebox.showwarning("Invalid Input", "Email address cannot be empty. Please try again.")

    tk.Button(email_window, text="OK", command=submit_email).pack(pady=5)


def ask_for_message(name, email):
    # Create a new window for message input
    message_window = tk.Toplevel(root)
    message_window.title("Enter Your Message")
    message_window.geometry("400x200")

    tk.Label(message_window, text="Please enter your message:").pack(pady=10)
    message_entry = tk.Text(message_window, height=5, width=40)
    message_entry.pack(pady=5)

    def submit_message():
        message = message_entry.get("1.0", tk.END).strip()
        if message:
            message_window.destroy()
            confirm_message(name, email, message)
        else:
            messagebox.showwarning("Invalid Input", "Message cannot be empty. Please try again.")

    tk.Button(message_window, text="Send", command=submit_message).pack(pady=5)


def confirm_message(name, email, message):
    try:
        # Create email
        msg = MIMEMultipart()
        msg['From'] = ADMIN_EMAIL
        msg['To'] = ADMIN_EMAIL
        msg['Subject'] = f"New Contact Message from {name}"

        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)
            server.send_message(msg)

        # Show success
        confirmation = (
            f"Thank you for contacting us!\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Message: {message}\n\n"
            f"Your message has been sent to our team.\n"
            "We will reach back to you within 24 hours."
        )
        messagebox.showinfo("Message Sent", confirmation)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")
    finally:
        root.destroy()


# Main application window
root = tk.Tk()
root.title("Online Shop")
root.geometry("300x150")

# Welcome message
tk.Label(root, text="Welcome to our online shop!").pack(pady=10)

# "Contact Us" button with color
contact_button = tk.Button(
    root,
    text="Contact Us",
    bg="blue",  # Background color
    fg="white",  # Text color
    font=("Arial", 12, "bold"),  # Font style
    command=ask_to_send_email
)
contact_button.pack(pady=20)

# Run the application
root.mainloop()