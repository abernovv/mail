import smtplib
import tkinter as tk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = "smtp.mail.ru"
SMTP_PORT = 465


accounts = {
     "почта1@mail.ru": "токен"
    ,"почта2@mail.ru": "токен",
     "почта3@mail.ru": "токен3"
}

def send_email():
    to_email = to_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    for from_email, password in accounts.items():
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(from_email, password)
                server.sendmail(from_email, to_email, msg.as_string())
            status_label.config(text=f"Письмо успешно отправлено с {from_email}")
        except Exception as e:
            status_label.config(text=f"Ошибка при отправке с {from_email}: {e}")

root = tk.Tk()
root.title("Отправка писем через Mail.ru")

tk.Label(root, text="Кому:").grid(row=0, column=0, padx=10, pady=5)
to_entry = tk.Entry(root, width=30)
to_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Тема:").grid(row=1, column=0, padx=10, pady=5)
subject_entry = tk.Entry(root, width=30)
subject_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Текст письма:").grid(row=2, column=0, padx=10, pady=5)
body_text = tk.Text(root, width=30, height=10)
body_text.grid(row=2, column=1, padx=10, pady=5)
send_button = tk.Button(root, text="Отправить", command=send_email)
send_button.grid(row=3, column=1, padx=10, pady=10)
status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
root.mainloop()