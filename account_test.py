import unittest
from account import User
from account import Credentials

class TestAccount (unittest.TestCase):

        def setUp(self):
        		'''
        		Function to create a user account before each test
        		'''
        		self.new_user = User('Moha','Moha','aenshtyn@aenshtyn.com','123')


        def test__init__(self):

        		self.assertEqual(self.new_user.first_name,'Moha')
        		self.assertEqual(self.new_user.last_name,'Moha')
                # self.assertEqual(self.new_user.email,'aenshtyn@aenshtyn')
        		self.assertEqual(self.new_user.password,'123')

        def test_save_user(self):

        		self.new_user.save_user()
        		self.assertEqual(len(User.user_list),1)

if __name__ ==  '__main__':
    unittest.main()
