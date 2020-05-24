from app import db

class User(db.Model):
    email = db.Column(db.String(120), index=True, unique=True, primary_key=True)

    def __repr__(self):
        return '<User {}>'.format(self.email)


class RssUrl(db.Model):
    url = db.Column(db.String(140), unique=True, primary_key=True)

    def __repr__(self):
        return '<RssUrl {}>'.format(self.body)
