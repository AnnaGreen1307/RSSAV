import feedparser
from flask import Markup

class RssParser():
    def validateUrl(self, _rssUrl):
        try:
            newsFeed = feedparser.parse(_rssUrl)
            if newsFeed:
                return True
        except Exception as e:
            return False


    def renderRss(self, _rssUrl):
        newsFeed = feedparser.parse(_rssUrl)
        rssHtmlContent = '<h1>RSS feed from "{}"</h1>'.format(_rssUrl)

        for entry in newsFeed.entries:
            #add whitespace before each entry
            rssHtmlContent += '<br><br><br>-------------------------------'
            
            #add timestamp
            rssHtmlContent += '<br>{}'.format(entry.published)
            
            #add title
            rssHtmlContent += '<br><h2><a href={}>{}</a></h2>'.format(entry.link, entry.title.encode('utf-8', 'ignore').decode('utf-8'))

            #add some details if they're exist
            if entry.summary != '':
                rssHtmlContent += '<br>{}'.format(entry.summary.encode('utf-8', 'ignore').decode('utf-8'))
        
        rssHtmlContent += '<br>===============================<br>'

        return rssHtmlContent

    
    def convertContent(self, _htmlContent):
        return Markup(_htmlContent)