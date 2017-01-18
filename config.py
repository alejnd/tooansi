
class Config(object):
    DEBUG        = False
    TESTING      = False
    CSRF_ENABLED = True
    SECRET_KEY   = '\x16\x91\xa4ZPL\xe6=%\xb6\x94\xe3<Cg\x1e\x00f21\x92\x8aq\x15'
    UPLOAD_FOLDER ='/tmp'
    MAX_CONTENT_LENGTH = 50 * 1024 #5Kb limit

class ProductionConfig(Config):
    HOST = '0.0.0.0'

class DevelopmentConfig(Config):
    HOST ='127.0.0.1'
    DEBUG    = True
    TESTING  = True

config = DevelopmentConfig()