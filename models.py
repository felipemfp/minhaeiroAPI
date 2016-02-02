from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    login = db.Column(db.String(50))
    password = db.Column(db.String(64))
    auth_key = db.Column(db.String(10))

    people = db.relationship('Person', backref='user', lazy='dynamic')
    transactions = db.relationship('Transaction', backref='user', lazy='dynamic')

    def __init__(self):
        pass

    def __repr__(self):
        return 'User {}'.format(self.user_id)


class Person(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    transactions = db.relationship('Transaction', backref='person', lazy='dynamic')
    transaction_items = db.relationship('TransactionItem', backref='person', lazy='dynamic')

    def __init__(self):
        pass

    def __repr__(self):
        return '<Person {}>'.format(self.person_id)


class Transaction(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    transaction_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, nullable=False)
    transaction_date = db.Column(db.DateTime)
    value = db.Column(db.Float)
    notes = db.Column(db.String(500))
    type = db.Column(db.String(1))
    done = db.Column(db.Boolean)

    transaction_items = db.relationship('TransactionItem', backref='transaction', lazy='dynamic')

    db.ForeignKeyConstraint(['user_id', 'person_id'], ['person.user_id', 'person.person_id'])

    def __init__(self):
        pass

    def __repr__(self):
        return '<Transaction {}.{}>'.format(self.user_id, self.transaction_id)


class TransactionItem(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, nullable=False)
    item_date = db.Column(db.DateTime)
    value = db.Column(db.Float)
    notes = db.Column(db.String(500))
    type = db.Column(db.String(1))
    done = db.Column(db.Boolean)

    db.ForeignKeyConstraint(['user_id', 'transaction_id'], ['transaction.user_id', 'transaction.transaction_id'])
    db.ForeignKeyConstraint(['user_id', 'person_id'], ['person.user_id', 'person.person_id'])

    def __init__(self):
        pass

    def __repr__(self):
        return '<Transaction Item {}.{}.{}>'.format(self.user_id, self.transaction_id, self.item_id)