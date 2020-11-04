from bs4 import BeautifulSoup
import requests
import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('GMAIL_USER')
EMAIL_PASSWORD = os.environ.get('GMAIL_PASS')
msg = EmailMessage()
msg['Subject'] = 'Graphics card Geforce RTX 3080'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'german.c86@gmail.com'
msg.set_content('Dear German, Placa de Video MSI GeForce RTX 3080 10GB GDDR6X VENTUS 3X OC + is IN STOCK!')

url = 'https://compragamer.com/producto/placa_de_video_msi_geforce_rtx_3080_10gb_gddr6x_ventus_3x_oc__10722?redir=1&nro_max=50'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
stock_button_text = soup.select_one('.card-btns__add').text.strip()

if stock_button_text == "Sumar al carrito":
    print("sending email...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
else:
    print("Product is NOT AVAILABLE")
