import os

SECRET_KEY = 'something'
DEBUG = True
DB_USERNAME = ''
DB_PASSWORD = ''
BLOG_DATABASE_NAME = ''
DB_HOST = ''
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
