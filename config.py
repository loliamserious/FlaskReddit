class Config(object):
    DEBUG = False
    TESTING = False

    db_username = 'bd9fd8a7a6122a'
    db_password = '7d868d4c'
    db_host = 'us-cdbr-east-04.cleardb.com'
    db_db = 'heroku_30e388627945153'

    SQLALCHEMY_DATABASE_URL = 'mysql://{}:{}@{}/{}'.format(db_username,db_password,db_host,db_db)


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass
