import os
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
print(account_sid)
print(auth_token)

client = Client(account_sid, auth_token)

def send_text(phone_number, sender_phone, message_body):
    message = client.messages.create(
        to=phone_number,
        from_=sender_phone,
        body=message_body)

def notify_admins(sender_phone, message_body):
    admins_numbers = [
        "7608778720"
    ]

    for admin_number in admins_numbers:
        send_text(admin_number, "+15012323138", "Heyoooo")
