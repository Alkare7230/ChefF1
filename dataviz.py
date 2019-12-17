#coding:utf-8

import sqlalchemy
import pymysql
import os
from flask import Flask, render_template, request

#____________________________________________________________________________________________________________________#
app = Flask(__name__)


class Database:
    def __init__(self):
        host = '127.0.0.1'
        user = "root"
        password = "shadow72"
        db = "def_f1"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def query_1(self):
        self.cur.execute("""SELECT name, driverRef, forename, number_id, dob, points, fastestLapTime, fastestLapSpeed, q1, laps FROM resultats
                            INNER JOIN pilote ON resultats.piloteId = pilote.piloteId
                            INNER JOIN qualif ON resultats.qualifyId = qualif.Id
                            INNER JOIN circuits ON resultats.raceId = circuits.raceId;""")
        result = self.cur.fetchall()
        return result




#____________________________________________________________________________________________________________________#



@app.route('/index', methods=['GET', 'POST'])
def accueil():
    def db_query():
        db = Database()
        q = db.query_1()
        return q
    res=db_query()

    print(res)
    return render_template('test.html', result=res, title='F1OLINE', content_type='application/csv')

@app.route('/pneu', methods=['GET', 'POST'])
def pneu():
    return render_template('pneu.html')

@app.route('/maps', methods=['GET', 'POST'])
def maps():
    return render_template('circuitmap.html')


if __name__ == "__main__":
    app.run(debug=True)
