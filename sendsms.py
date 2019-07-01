# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''#your account sid can be obtained from twilio dashboard
auth_token = ''#your authentication token can be obtained from twilio dashboard
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="heey boy",
                     from_='+xxxxxxxxx',
                     to='+9xxxxxxxxx'
                 )

print(message.sid)
