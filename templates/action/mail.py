import smtplib

def action(msg):
    fromaddr = "hackdayrack@gmail.com"
    toaddrs = "{{toaddr}}"
    subject = "{{subject}}"

    #provide gmail user name and password
    username = 'username'
    password = 'password'

    # functions to send an email
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
