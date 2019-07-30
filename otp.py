from twilio.rest import Client
import random


otp_g = random.randint(1000, 9999)
print(otp_g)
a = "ACd0310c98f582e1231f79acbeeae8bfa5"
b = "bd8c5a962a98506d6701b2fd24cfba42"
abc = Client(a, b)
abc.messages.create(from_="(202) 915-7785", to="919495415120", body="hai...your verification code is "+str(otp_g))




