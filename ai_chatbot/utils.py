# set up for sending WhatsApp message through Twilio API


import logging
from twilio.rest import Client
from decouple import config      #used to access private credentials stored in .env file


account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = config('TWILIO_NUMBER')

# Configuring the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)     # creating a logger object

# Sending message through Twilio API
def send_message(to_number, body_text):
    try:
        message = client.messages.create(
            from_=f"whatsapp:{twilio_number}",
            body=body_text,
            to=f"whatsapp:{to_number}"
            )
        logger.info(f"Message sent to {to_number}: {message.body}")
    except Exception as e:
        logger.error(f"Error sending message to {to_number}: {e}")
