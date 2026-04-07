import psycopg2
from flask import Flask

app = Flask(__name__)

DB_URL = "postgresql://flask_lab_db_ijxs_user:y2qMtgXX852yW4IlqzJ2PC0MxGTnYQLr@dpg-d7a7293uibrs73fralo0-a/flask_lab_db_ijxs"

@app.route('/')
def index():
    return 'Hello World from Andrew MacRossie in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://flask_lab_db_ijxs_user:y2qMtgXX852yW4IlqzJ2PC0MxGTnYQLr@dpg-d7a7293uibrs73fralo0-a/flask_lab_db_ijxs")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('YOUR_FIRST', 'YOUR_LAST', 'CU Boulder', 'YOUR_TEAM', 3308);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    conn.close()

    response = '<table border="1"><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>'
    for row in records:
        response += '<tr>'
        for field in row:
            response += '<td>' + str(field) + '</td>'
        response += '</tr>'
    response += '</table>'
    return response

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('DROP TABLE Basketball;')
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"

