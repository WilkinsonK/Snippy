import unittest


class BaseTests(unittest.TestCase):

    def test_sanity01(self):
        self.assertEquals((2 + 2), 4)

    def test_sanity02(self):
        self.assertNotEquals('UP', 'DOWN')
