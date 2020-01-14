'''
@Description: 
@Author: lonel
@Date: 2020-01-14 10:48:01
@LastEditors: lonel
'''
from flask import Blueprint

bp = Blueprint('api', __name__)

# 写在最后是为了防止循环导入，ping.py文件也会导入 bp
from app.api import ping