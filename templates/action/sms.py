from twilio.rest import TwilioRestClient

def action(sms):
    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "{{account_sid}}"
    AUTH_TOKEN = "{{auth_token}}"
    from_ = "{{from}}"
    to = "{{to}}"
    
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    
    message = client.messages.create(
        body= sms, 
        to=to,
        from_=from_,
    )
