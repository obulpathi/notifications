import requests

def action(msg):
    VERB = "{{verb}}"
    URL = "{{url}}"

    requests.request(VERB, URL, data={'msg': msg})
