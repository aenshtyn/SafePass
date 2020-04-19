import unittest
from account import User
from account import Credentials

class TestAccount (unittest.TestCase):

        def setUp(self):
        		'''
        		Function to create a user account before each test
        		'''
        		self.new_user = User('Mary','Ng\'ang\'a','pswd100')


if __name__ ==  '__main__':
    unittest.main()
