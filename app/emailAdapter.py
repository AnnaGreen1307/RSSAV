from flask import Flask
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class EmailAdapter():
    def sendMessage(self, _usersList, _rssHtmlContent):
        ret = ''

        try:
            for user in _usersList:
                message = Mail(
                    from_email = os.environ.get('FROM_EMAIL'),
                    to_emails = user.email,
                    subject = 'Rss2eMail demo app',
                    html_content = _rssHtmlContent)
        
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                if response.status_code != 202:
                    ret += '<br>Unable to send the message to "{}", because of "{}"'.format(user.email, response.body)
                else:
                    ret += '<br>Message sent for "{}"'.format(user.email)
                
        except Exception as e:
            ret += 'Exception catched: "{}"'.format(e)

        return ret