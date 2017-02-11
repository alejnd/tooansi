
import os

class Config(object):
    DEBUG        = False
    TESTING      = False
    CSRF_ENABLED = True
    SECRET_KEY   = os.urandom(24)
    UPLOAD_FOLDER ='/tmp'
    MAX_CONTENT_LENGTH = 50 * 1024 #5Kb limit

class ProductionConfig(Config):
    HOST = '0.0.0.0'

class DevelopmentConfig(Config):
    HOST ='127.0.0.1'
    DEBUG    = True
    TESTING  = True

config = ProductionConfig()
