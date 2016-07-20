import os
import unittest
from app import create_app,app_config,get_db,allowed_file

config=app_config.get(os.environ.get('FLASK_CONIFG','testing'))

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app=create_app(config)
        self.ctx=app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def testGetDb(self):
        db=get_db()
        self.assertEqual(db.name,'torrentstash_test')

    def testAllowFileWithTorrentFileExtension(self):
        result=allowed_file('Sample.torrent')
        self.assertTrue(result)

    def testAllowFileWithPdfFileExtension(self):
        result=allowed_file('Sample.pdf')
        self.assertFalse(result)

    def testAllowFileWithJpgFileExtension(self):
        result=allowed_file('Sample.jpg')
        self.assertFalse(result)

    def testAllowFileWithMp3FileExtension(self):
        result=allowed_file('Sample.mp3')
        self.assertFalse(result)

    def testAllowFileWithMp4FileExtension(self):
        result=allowed_file('Sample.mp4')
        self.assertFalse(result)

    def testAllowFileWithPngFileExtension(self):
        result=allowed_file('Sample.png')
        self.assertFalse(result)
