class User:

    user_list = []

    def __init__(self,first_name,last_name,email, password):


        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password = password

    def tearDown(self):
            User.user_list = []


    def save_user(self):
            User.user_list.append(self)

class Credentials:

    credential_list = []

    def __init__(self, account_name, username, password):

        self.account_name = account_name
        self.username = username
        self.password = password

    def save_credentials(self):
        Credentials.credential_list.append(self)

    def delete_credential(self):
        User.credential_list.remove(self)


    @classmethod
    def find_by_account_name (cls, account_name):
        for credential in cls.Credentials:
            if credential.username == username
            return credential

    @classmethod
    def display_credentials(cls)

    return cls.credential_list
