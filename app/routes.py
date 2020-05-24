from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import AddRssUrl, AddUser
from app.models import RssUrl, User
from app.rssParser import RssParser
from app.emailAdapter import EmailAdapter


@app.route('/')
@app.route('/index')
def index():
    rssUrlsList = RssUrl.query.all()
    usersList = User.query.all()

    htmlContent = ''
    parser = RssParser()
    for rssUrl in rssUrlsList:
        htmlContent += parser.renderRss(_rssUrl=rssUrl.url)

    rssPreviewHtml = parser.convertContent(htmlContent)
    return render_template('index.html', title='Home', rssUrlsList=rssUrlsList, usersList=usersList, rssPreviewHtml=rssPreviewHtml)


@app.route('/addrssurl', methods=['GET', 'POST'])
def addRssUrl():
    form = AddRssUrl()
    if form.validate_on_submit():
        if RssUrl.query.filter_by(url=form.rssUrl.data).first():
            flash('RSS URL "{}" already in list'.format(form.rssUrl.data))
        else:
            rssParser = RssParser()
            if not rssParser.validateUrl(form.rssUrl.data):
                flash('Not valid RSS URL "{}". Operation failed'.format(form.rssUrl.data))
            else:
                rssUrl = RssUrl(url=form.rssUrl.data)
                db.session.add(rssUrl)
                db.session.commit()
                flash('New RSS URL "{}" added into DB'.format(form.rssUrl.data))
                return redirect(url_for('index'))
    return render_template('addRssUrl.html',  title='Add RSS URL', form=form)


@app.route('/adduser', methods=['GET', 'POST'])
def addUser():
    form = AddUser()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email "{}" already in list'.format(form.email.data))
        else:
            user = User(email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('New email "{}" added into DB'.format(form.email.data))
            return redirect(url_for('index'))
    return render_template('addUser.html',  title='Add Email', form=form)


@app.route('/sendmessage')
def sendMessage():
    rssUrlsList = RssUrl.query.all()
    usersList = User.query.all()

    htmlContent = ''
    parser = RssParser()
    for rssUrl in rssUrlsList:
        htmlContent += parser.renderRss(_rssUrl=rssUrl.url)

    if not htmlContent:
        flash('No RSS content for sharing')
    elif not usersList:
        flash('No Emails to receive the message')
    else:
        emailAdapter = EmailAdapter()
        flash(emailAdapter.sendMessage(usersList, htmlContent))
    
    return redirect(url_for('index'))