#Não funcionou

from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open("templat.html", "r") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%D/%M/%Y")
    corpo_msg = template.substitute(nome="Nicolas", data=data_atual)

msg = MIMEMultipart()
msg["from"] = "Nicolas Donada"
msg["to"] = "nicolasdonada12@gmail.com"
msg["subject"] = "Atenção: Testando envio de emails"

corpo = MIMEText(corpo_msg, "html")
msg.attach(corpo)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login()
    smtp.send_message(msg)
    print("Email enviado com sucesso!!!")