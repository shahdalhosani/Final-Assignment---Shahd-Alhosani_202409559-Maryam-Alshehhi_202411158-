#This class stores user information
class User:
    def __init__(self, user_id, name, email, password, access_type="Standard"):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.access_type = access_type

    #Getter and setter for user ID
    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    #Getter and setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    #Getter and setter for email
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    #Getter and setter for password
    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    #Getter and setter for access type
    def get_access_type(self):
        return self.access_type

    def set_access_type(self, access_type):
        self.access_type = access_type

    #Check if email and password are correct
    def login(self, email, password):
        return self.email == email and self.password == password

    #Upgrade user from Standard to Premium
    def upgrade_access(self):
        self.access_type = "Premium"
