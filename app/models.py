from datetime import datetime

from app import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(database.Model, UserMixin):
    __tablename__ = 'Users'

    id = database.Column(database.Integer, autoincrement = True, primary_key = True)
    name = database.Column(database.String(100), nullable=False, unique = True)
    salary = database.Column(database.Integer, nullable=False)
    password = database.Column(database.String(60), default = 'dole')
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

    @property
    def total_years(self):

        sum_ = 0

        for empl in Employment.query.filter_by(user_id = self.id).all():

            sum_ += empl.years_active

        return sum_


    def __repr__(self):
        return '<User: {}>'.format(self.name)

class Unit(database.Model):

    __tablename__ = 'Units'

    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(50), unique = True)
    users = database.relationship('User', secondary='Employments', backref='units')


    @property
    def total_years(self):

        sum_ = 0

        for empl in Employment.query.filter_by(unit_id = self.id).all():

            sum_ += empl.years_active
            
        return sum_


class Employment(database.Model):

    __tablename__ = 'Employments'
    
    id = database.Column(database.Integer, primary_key = True)

    #    employent extra details
    title = database.Column(database.String(50), nullable = True)
    years_active = database.Column(database.Integer, nullable=False)

    # ForeignKeys
    user_id = database.Column(database.Integer, database.ForeignKey('Users.id'))
    unit_id = database.Column(database.Integer, database.ForeignKey('Units.id'))

    # rels
    user = database.relationship('User', backref='units_rel')
    unit = database.relationship('Unit', backref='users_rel')

