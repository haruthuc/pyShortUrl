
import imghdr
import os
import sys
import unittest
import imghdr

from ShortUrl.v_gd import Vgd

class TestVgd(unittest.TestCase):

    def setUp(self):
        self.test_long_url = 'http://www.parthbhatt.com/blog/'
        self.test_short_url = 'http://v.gd/mfu3Ul'

    def test_shorten_url(self):
        service = Vgd()
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_expand_url(self):
        service = Vgd()
        generated_long_url = service.expand_url(self.test_short_url)

        self.assertEqual(self.test_long_url, generated_long_url)


if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVgdAndIsgd)
    unittest.TextTestRunner(verbosity=2).run(suite)
