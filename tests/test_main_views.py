import os
import unittest
from app import create_app,app_config

config=app_config.get(os.environ.get('FLASK_CONIFG','testing'))

class IndexViewTestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app(config)
        self.client=self.app.test_client()

    def tearDown(self):
        self.app=None

    def testRedirectFromRootToHomePage(self):
        result=self.client.get('/')
        self.assertTrue('You should be redirected automatically to target URL:' in result.data)

    def testRedirectToHomeAfterUrlRewrite(self):
        result=self.client.get('/main')
        self.assertTrue('You should be redirected automatically to target URL:' in result.data)

    def testHomePageStatusCode(self):
        result=self.client.get('/main/')
        self.assertEqual(result.status_code,200)

    def testHomePageResult(self):
        result=self.client.get('/main/')
        self.assertTrue('Search for your favorite torrents and magnets !' in result.data)

class TorrentListViewTestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app(config)
        self.client=self.app.test_client()

    def tearDown(self):
        self.app=None

    def testRedirectAfterUrlRewrite(self):
        result=self.client.get('/main/torrents')
        self.assertTrue('You should be redirected automatically to target URL:' in result.data)

    def testTorrentResultStatusCode(self):
        result=self.client.get('/main/torrents/')
        self.assertEqual(result.status_code,200)

    def testTorrentResultMimeType(self):
        result=self.client.get('/main/torrents/')
        self.assertEqual(result.headers['Content-Type'],'application/json')

    def testNonEmptyTorrentResult(self):
        result=self.client.get('/main/torrents/')
        self.assertNotEqual(result.data,'{}')

    def tetEmptyTorrentResult(self):
        result=self.client.get('/main/torrents/')
        self.assertEqual(result.data,'{}')

