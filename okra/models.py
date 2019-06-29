from okra import db, bcrypt
from datetime import datetime

class User(db.Model):
    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        email address
        password (hashed using Bcrypt)
        authenticated flag (indicates if a user is logged in or not)
        date that the user registered on
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.Binary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String, default='user')
    #roles: user(default) - associate(has ecobusiness registered) - admin

    def __init__(self, email, plaintext_password, role='user'):
        self.email = email
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password)
        self.authenticated = False
        self.registered_on = datetime.now()
        self.role = role

    def set_password(self, plaintext_password):
        self.hashed_password = bcrypt.generate_password_hash(plaintext_password)

    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.hashed_password, plaintext_password)

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the id of a user to satisfy Flask-Login's requirements."""
        return str(self.id)

    def __repr__(self):
        return '<User {}>'.format(self.email)

from okra import db, bcrypt
from datetime import datetime

class Business(db.Model):
    """
    Class that represents a eco business registered in the application

    The following attributes of a registered business are stored in this table:
        email address
        date that the business was registered on
    """

    __tablename__ = 'ecobusiness'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    website = db.Column(db.String, unique=True, nullable=False)
    location = db.Column(db.String, nullable=False)
    telephonenumber = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=False)
    subscriptionplan = db.Column(db.String, nullable=False) 
    email = db.Column(db.String, unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    updated_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, userid, website, location, telephonenumber, 
        comment, subscriptionplan, email, registered_on, updated_on):
        self.name = name
        self.userid = userid
        self.website = website
        self.location = location
        self.telephonenumber = telephonenumber
        self.comment = comment
        self.subscriptionplan = subscriptionplan
        self.email = email
        self.registered_on = registered_on
        self.updated_on = updated_on
       

    def __repr__(self):
        return '<Business {}>'.format(self.name)



