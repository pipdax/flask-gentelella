# -*- coding: utf-8 -*-
#__author__="pipdax"

from flask import Flask
from flask import request
from flask import Response
from flask import jsonify

import sqlite3

import json

def get_db():
    db = sqlite3.connect('mydb.db')
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    # cur = db.execute("SELECT * FROM cpu WHERE id>=1")
    db.commit()
    rv = cur.fetchall()
    db.close()
    return (rv[0] if rv else None) if one else rv

def my_data():
	'''
	res = query_db("SELECT * FROM weather")

	return jsonify(month=[x[0] for x in res],
				evaporation=[x[1] for x in res],
				precipitation=[x[2] for x in res])
	'''
	data = {"spam": "foo", "parrot": 42}
	in_json = json.dumps(data)
	return in_json

def my_charts():
	return "hello world 111"