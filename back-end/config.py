'''
@Description: 
@Author: lonel
@Date: 2020-01-14 10:41:34
@LastEditors  : lonel
'''
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))



class Config(object):
    pass