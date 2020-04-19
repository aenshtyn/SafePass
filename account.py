global user_list

class User:

    user_list = []

    def __init__(self,first_name,last_name,email, password):


        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def tearDown(self):
            User.user_list = []


    def save_user(self):
            User.user_list.append(self)

class Credentials:

    credentials_list = []
    user_credentials_list = []
	@classmethod
	def check_user(cls,first_name,password):

		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

    def __init__(self, account_name, username, password):

        self.account_name = account_name
        self.username = username
        self.password = password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        User.credentials_list.remove(self)

    def generate_password(size=6, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass


    @classmethod
    def find_by_account_name (cls, account_name):
            for credentials in cls.Credentials:
                    if credential.account_name == account_name:
                            return credential

    @classmethod
    def display_credentials(cls, username):

            user_credentials_list = []

            for credentials in cls.credentials_list:
                if credentials.username == username:
                    user_credentials_list.append(credentials)
            return user_credentials_list
