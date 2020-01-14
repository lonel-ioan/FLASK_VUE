'''
@Description: 
@Author: lonel
@Date: 2020-01-14 10:46:40
@LastEditors: lonel
'''
from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册 blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app