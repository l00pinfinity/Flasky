import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hardtoguessstring'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    BLOGGING_MAIL_PREFIX = '[Blogging]'
    BLOGGING_MAIL_SENDER ='nathanpykimutai@gmail.com' #os.environ.get('MAIL_USERNAME')
    BLOGGING_ADMIN =  'nathanpykimutai@gmail.com'
    BLOGGING_MAIL_SUBJECT_PREFIX = "[Blogging]"
    BLOGGING_POSTS_PER_PAGE = 10
    BLOGGING_COMMENTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):

    DEBUG = True
    MAIL_SERVER = 'smtp.google.com'
    MAIL_PORT = 587
    #MAIL_USE_SSL = True
    MAIL_USE_TLS = True
    MAIL_PASSWORD = '@Helloworld254'
    MAIL_USERNAME = 'nathanpykimutai@gmail.com'
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(base_dir,'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #SQLALCHEMY_ECHO = True

class TestingConfig(Config):

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(base_dir,'data-test.sqlite')
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://cbuser:cbpass@localhost:3306/cookbook"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(base_dir,'data.sqlite')



config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}

