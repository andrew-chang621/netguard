import sys
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = sys.argv["TWILIO_ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token = sys.argv["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)


def send_text(phone_number, sender_phone, message_body):
    message = client.messages.create(
        to="+15558675309",
        from_="+15017250604",
        body="Hello from Python!")

    print(message.sid)


def notify_admins(sender_phone, message_body):
    admins_numbers = [
        "7072921668"
    ]

    for admin_number in admins_numbers:
        send_text(admin_number, "", "Heyoooo")
