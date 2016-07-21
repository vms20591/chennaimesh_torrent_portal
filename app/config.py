import os
import base64

class Config(object):
    #secret key for csrf purpose and etc.,
    SECRET_KEY = os.environ.get('SECRET_KEY') or base64.b64encode(os.urandom(20))

    #default debug setting
    DEBUG=True
    TESTING=False

    ALLOWED_EXTENSIONS = set(['torrent'])
    BASE_DIR=os.environ.get('FLASK_UPLOAD_DIR') or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    UPLOAD_FOLDER = os.path.join(BASE_DIR,'uploads')

    MONGO_DBNAME="torrentstash"

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

class DevelopmentConfig(Config):
    #switching off test config
    TESTING=False

class TestingConfig(Config):
    #switching to test config
    TESTING=True
    
    MONGO_DBNAME="torrentstash_test"
	
class ProductionConfig(Config):
    #swtiching off debug and testing
    DEBUG=False
    TESTING=False

    MONGO_DBNAME="torrentstash_prod"

#configuration factor object
app_config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
}
