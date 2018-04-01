# -*- coding: utf-8 -*-
#__author__="pipdax"

from flask import Flask
from flask import request
from flask import Response

import json


def echarts():
	'''
    datas = {
		"data":[
			{"name":"allpe","num":100},
			{"name":"peach","num":123},
			{"name":"Pear","num":234},
			{"name":"avocado","num":20},
			{"name":"cantaloupe","num":1},
			{"name":"Banana","num":77},
			{"name":"Grape","num":43},
			{"name":"apricot","num":0}
		]
	}
    content = json.dumps(datas)
    resp = Response_headers(content)
    #return resp
    '''
	return "hello world 222"