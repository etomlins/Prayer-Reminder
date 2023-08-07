import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

number = os.getenv('PHONE_NUMBER')
email = os.getenv('EMAIL')
passw = os.getenv('PASSWORD')

carriers = {
	'att':    '@mms.att.net',
	'tmobile':'@tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

people = {
	'me':number
}

def send(subj,body):

	to_number = people['me'].format(carriers['tmobile'])
	auth = (email, passw)

	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	msg = EmailMessage()
	msg.set_content(body)
	subj = subj.replace("\n", "").replace("\r", "")
	msg['Subject'] = subj

	server.sendmail(auth[0], to_number, msg.as_string())

