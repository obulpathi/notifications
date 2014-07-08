from twilio.rest import TwilioRestClient

def action(url):
    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "{{account_sid}}"
    AUTH_TOKEN = "{{auth_token}}"
    from_ = "{{from}}"
    to = "{{to}}"
    
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    
    message = client.messages.create(
        to=to,
        from_=from_,
        media_url= url
    }
