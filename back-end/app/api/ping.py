'''
@Description: 
@Author: lonel
@Date: 2020-01-14 10:48:18
@LastEditors: lonel
'''
from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify('Pong!')