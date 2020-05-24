from app import app, db
from app.models import User, RssUrl

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'RssUrl': RssUrl}

'''
from flask import Flask
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import feedparser

app = Flask(__name__)
fromEmail = 'avolkova@bizteo.com'
emailSubject = 'RSS to eMail demo app'


def sendMessage(_targetEmail, _rssHtmlContent):
    message = Mail(
        from_email = fromEmail,
        to_emails = _targetEmail,
        subject = emailSubject,
        html_content = _rssHtmlContent)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        #print(response.status_code)
        #print(response.body)
        #print(response.headers)
        return '{}<br><br>{}<br><br>{}'.format(response.status_code, response.body, response.headers)
    except Exception as e:
        return e.body
        #print(e.body)


@app.route('/sendmail')
def sendmail():
    rssHtmlContent = 'Some content sent'
    return sendMessage('alessandrocagliostrobalsamo@gmail.com', rssHtmlContent)


def parseRss(_rssUrl):
    newsFeed = feedparser.parse(_rssUrl)

    rssHtmlContent = '<h1>RSS feed from "{}"</h1>'.format(_rssUrl)

    for entry in newsFeed.entries:
        #add whitespace before each entry
        rssHtmlContent += '<br><br><br>-------------------------------'
        
        #add timestamp
        rssHtmlContent += '<br>{}'.format(entry.published)
        
        #add title
        rssHtmlContent += '<br><h2><a href={}>{}</a></h2>'.format(entry.link, entry.title)

        #add some details if they're exist
        if entry.summary != '':
            rssHtmlContent += '<br>{}'.format(entry.summary)
    
    rssHtmlContent += '<br>===============================<br>'

    return rssHtmlContent


@app.route('/')
@app.route('/index')
def index():
    htmlContent = parseRss('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
    htmlContent += parseRss('https://habr.com/en/rss/all/all/')

    sendMessage('alessandrocagliostrobalsamo@gmail.com', htmlContent)
    return htmlContent
'''