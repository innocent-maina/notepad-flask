# config.py
import os

database = os.getenv('SQLALCHEMY_DATABASE_URI')

class Config(object):
    """
    Common configurations
    """
    SECRET_KEY=os.getenv('SECRET_KEY')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True



class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    SQLALCHEMY_ECHO = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}