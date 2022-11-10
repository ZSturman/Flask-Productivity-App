
class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'f5ae3536d2465afe1fe3bc35138172d1'

    ## SQLalchemy db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

    ## MySQL db
    #               'mysql+pymysql://username:password@localhost/db_name'
    """ SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:MxR2epTP@localhost/mapps' """
    
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    EMAIL_ADDRESS = "zasturman@gmail.com"
    EMAIL_PASSWORD = "fuelczosdhmdqfzw"
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False

    SESSION_COOKIE_SECURE = True

    UPLOAD_FOLDER = '/static/images'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False

