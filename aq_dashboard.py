"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)
api = openaq.OpenAQ()


def get_results():
    '''Gets results from api'''
    _, data = api.measurements(parameter='pm25')
    results = data['results']
    utc_value_tuples = [(result['date']['utc'], result['value'])
                        for result in results]
    return utc_value_tuples


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True,)
    datetime = DB.Column(DB.String, nullable=False)
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'Record: {self.id}, {self.datetime}, {self.value}'


@app.route('/')
def root():
    """Base view."""
    # records = Record.query.filter(Record.value >= 18).all()
    record = Record.query.all()
    return str(record)


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    tuples = get_results()
    for tuple in tuples:
        record = Record(datetime=tuple[0], value=tuple[1])
        DB.session.add(record)
    DB.session.commit()
    return root()
