#!/usr/bin/env python3.8
from locker import User, Credentials

def create_new_user(username,password):
    '''
    Function to create a new contact
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def display_users():
    '''
    Function to display existing user
    '''
    return User.display_users()

def login_user(username,password):
    '''
    A function thay checks whether the user exusts and then login the user
    '''
    check_user = User.verify_user(username,password)
    return check_user

def create_new_credentials(account,userName,password):
    '''
    Function that creates new credentials for a given account for the user
    '''
    new_credentials = Credentials(account,userName,password)
    return new_credentials
def save_credentials(credentials):
    '''
    Function that saves credentials created to the credential_list
    '''
    credentials.save_credential()

def display_account_details():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def delete_credential(credentials):
    '''
    Function that deletes credentials from the credential_list
    '''
    credentials.delete_credentials()

def check_credentials(userName):
    '''
    Function that checks if a credential exists with that username and return true or false
    '''
    return Credentials.credential_exist(userName)

def find_credential(userName):
    '''
    Function that finds a credentials by use of userName and returns all the information
    '''
    return Credentials.find_credential(userName)

def get_Password():
    '''
    Function that generates a password for the user
    '''
    auto_password = Credentials.getPassword()
    return auto_password