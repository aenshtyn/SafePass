import unittest
import pyperclip
from account import User
from account import Credentials

class TestUser (unittest.TestCase):

        def setUp(self):
        		self.new_user = User('Moha','Moha','aenshtyn@aenshtyn.com','123')


        def test__init__(self):

        		self.assertEqual(self.new_user.first_name,'Moha')
        		self.assertEqual(self.new_user.last_name,'Moha')
                # self.assertEqual(self.new_user.email,'aenshtyn@aenshtyn.com')
        		self.assertEqual(self.new_user.password,'123')

        def test_save_user(self):

        		self.new_user.save_user()
        		self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):

        def test_check_user(self):

        		self.new_user = User('Moha','Moha','aenshtyn@aenshtyn.com','123')
        		self.new_user.save_user()
        		user2 = User('Tom','Boy','Tom@mail.com','987')
        		user2.save_user()

        		for user in User.users_list:
        			if user.email == user2.email and user.password == user2.password:
        				current_user = user.first_name
        		return current_user

        		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))


        def setUp(self):

    		    self.new_credential = Credential('Moha','Facebook','aenshtyn','987410')

    	def test__init__(self):

        		self.assertEqual(self.new_credential.user_name,'Moha')
        		self.assertEqual(self.new_credential.site_name,'Facebook')
        		self.assertEqual(self.new_credential.account_name,'aenshtyn')
        		self.assertEqual(self.new_credential.password,'987410')



    	def test_save_credentials(self):

    		self.new_credential.save_credentials()
    		twitter = Credential('Moha','Twitter','aenshtyn','654321')
    		twitter.save_credentials()
    		self.assertEqual(len(Credential.credentials_list),2)


    	def test_display_credentials(self):

    		self.new_credential.save_credentials()
    		twitter = Credential('Moha','Twitter','aenshtyn','987410')
    		twitter.save_credentials()
    		gmail = Credential('Moha','Gmail','aenshtyn','123456')
    		gmail.save_credentials()
    		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

    	def test_find_by_account_name(self):

    		self.new_credential.save_credentials()
    		twitter = Credential('Moha','Twitter','aenshtyn','123456')
    		twitter.save_credentials()
    		credential_exists = Credential.find_by_site_name('Twitter')
    		self.assertEqual(credential_exists,twitter)

if __name__ ==  '__main__':
    unittest.main()
