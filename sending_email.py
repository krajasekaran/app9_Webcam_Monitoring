import imghdr
import smtplib
from email.contentmanager import maintype, subtype
from email.message import EmailMessage

PASSWORD = ""
SENDER = ""
RECEIVER = ""

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer detected"
    email_message.set_content("New Customer emailed")

    with open(f"{image_path}", "rb") as file:
        content = file.read()

    email_message.add_attachment(content,maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

    print("Email sent")

if __name__ == "__main__":
    send_email(image_path="images/222.png")
