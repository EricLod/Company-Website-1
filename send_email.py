import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    msg = message

    username = "jew.user@gmail.com"
    password = "yjphpritxcnskijz"

    receiver = "jew.user@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)