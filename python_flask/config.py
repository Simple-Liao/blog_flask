import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config():

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:AVAava2020@localhost:3306/flaskblog?charset=utf8'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = '123456asd'