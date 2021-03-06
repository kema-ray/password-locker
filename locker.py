import random
import string
import pyperclip

class User:
    '''
    Class that generates new instances of users
    '''
    user_list = []
    def __init__(self,username,password):
        '''
        __init__ method that helps us define properties for our objects
        '''
        self.username = username
        self.password = password
    def save_user(self):
        '''
        save_user method saves user objects intouser_list
        '''
        User.user_list.append(self)
    @classmethod
    def display_users(cls):
        '''
        A method that returns the user list
        '''
        return cls.user_list
    def delete_user(self):
        '''
        A method that deletes a saved user from the user_list
        '''
        User.user_list.remove(self)
    @classmethod
    def verify_user(cls,username,password):
        '''
        A method to verify the user is in our user_list or not 
        '''
        person= ""
        for user in User.user_list:
            if(user.username == username  and user.password == password):
                person == user.username
        return person

class Credentials():
    '''
    class that generates new instances of contacts
    '''
    credentials_list = []
    def __init__(self,account,userName,password):
        '''
        Method that helps us define properties for our objects
        '''
        self.account = account
        self.userName = userName
        self.password = password
    def save_credential(self):
        '''
        A method that saves credential objects into credentials_list
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        A method that deletes an accounts credentials from the credential list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls,userName):
        '''
        A method that uses the userName and returns a credential that matches te username.
        '''
        for credential in cls.credentials_list:
            if credential.userName == userName:
                return credential

    @classmethod
    def credential_exist(cls,userName):
        '''
        A method that checks if a credential exists in the credential_list and it returns a true or a false
        '''
        for credential in cls.credentials_list:
            if credential.userName == userName:
                return True
        return False
    
    @classmethod
    def display_credentials(cls):
        '''
        Amethod that returns all items in the credentials_list
        '''
        return cls.credentials_list

    def generate_password(stringLength=15):
        '''
        Generate a random password string that cnsists letters,digits and special characters
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "@#$%~&*"
        return ''.join(random.choice(password) for i in range(stringLength))
    
    @classmethod
    def copy_password(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)