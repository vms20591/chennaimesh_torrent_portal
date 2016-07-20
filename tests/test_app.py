import os
import unittest
from app import create_app,app_config

config=app_config.get(os.environ.get('FLASK_CONIFG','testing'))

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateApp(self):
        app=create_app(config)
        self.assertIsNotNone(app)

    def testCreateAppName(self):
        app=create_app(config)
        self.assertEqual(app.name,'app')
