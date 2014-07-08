from twilio.rest import TwilioRestClient

def action():
    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "{{account_sid}}"
    AUTH_TOKEN = "{{auth_token}}"
    from_ = "{{from}}"
    to = "{{to}}"
    url = "{{url}}"
    
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    
    call = client.calls.create(from_=from_, to=to, url = url)
