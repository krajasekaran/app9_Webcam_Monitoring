import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(subject, body, to_email, attachment_file):
    # Gmail configuration
    gmail_user = ''
    gmail_password = ''

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body text
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file
    try:
        with open(attachment_file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment_file}')
            msg.attach(part)
    except Exception as e:
        print(f"Could not attach file: {e}")
        return

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(gmail_user, gmail_password)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email_with_attachment(
        subject="Test Email with Attachment",
        body="Please find the attached file.",
        to_email="krajasekaran86@gmail.com",
        attachment_file="/Users/krajasekaran/Desktop/python/pythonProject/app9_Webcam_Monitoring/images/6.png"
    )
