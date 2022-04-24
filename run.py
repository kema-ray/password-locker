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

def gen_password():
    '''
    Function that generates a password for the user
    '''
    default_password = Credentials.generate_password()
    return default_password

def locker():
    print("Hello Welcome to the Password Locker \n Enter one of the folllowing in order to proceed.\n CA ---- Create new Account EA--- Already has an existing Account")
    short_code = input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('-'*50)
        username = input("UserName: ")
        while True:
            print("TP- Type your own password:\n GP - Generate for me a password:")
            choose_password = input().lower().strip()
            if choose_password == 'tp':
                password = input("Enter Password.\n")
                break
            elif choose_password == 'gp':
                password = gen_password()
                break
            else:
                print("Try again!Invalid password!!")
        save_user(create_new_user(username,password))
        print("-"*50)
        print(f"Hello {username},your login was successful! Your password is:{password}")
        print("-"*40)
    elif short_code == "ea":
        print("-"*35)
        print("Enter your username amd password to sign in:")
        print("-"*35)
        username=input("username: ")
        password=input("password: ")
        # signin = login_user(username,password)
        # if login_user == signin
        print(f"Hello {username}.Welcome to the password locker")

    while True:
        print("Use these short codes:\n NC-New Credential\n DC-Display credentials\n SC-Search credential\n GP-Generate random password\n D-Delete credential\n EX-exit\n")
        short_code =input().lower().strip()
        if short_code == "nc":
            print("Create new credential")
            print("-"*30)
            print("Enter Account name ...")
            account = input().lower()
            print("Enter your username:")
            userName = input()
            while True:
               print("TP-Type password GP-Generate password")
               choose_password = input().lower().strip()
               if choose_password == "tp":
                  password = input("Enter your password\n")
                  break
               elif choose_password == "gp":
                   password = gen_password()
                   break
               else:
                   print("Invalid password")
            save_credentials(create_new_credentials(account,userName,password))
            print(f"Account credentials for:{account} -UserName: {userName} -Password: {password} successfully created")       
        
        elif short_code == "dc":
            if display_account_details():
                print("This is the list of accounts saved: ")
                print("-"*40)
                for user in display_account_details():
                    print(f"Account:{user.account} UserName:{username} Password:{password}")
                print("-"*40)
            else:
                print("No such credentials are saved yet......")    

        elif short_code == "sc":
            print("Enter the userName you want to search for")
            input_name = input().lower()
            if find_credential(input_name):
                search_credential = find_credential(input_name)
                print(f"User Name: {search_credential.userName}")
                print("-"*60)
            else:
                print("That credential is unavailable")
        
        elif short_code == "d":
            print("Enter user name of the credentials to be deleted")
            input_name = input().lower()
            if find_credential(input_name):
                search_credential = find_credential(input_name)
                print("-"*50)
                search_credential.delete_credentials()
                print(f"The stored credentials for : {search_credential.userName} successfully removed")
            else:
                print("That credential does not exist")    
        
        elif short_code == "gp":
            password = gen_password()
            print(f"{password} Password has been generated successfully. Enjoy using the password generated")
        
        elif short_code == "ex":
            print("Thank you for using this site..Welcome again")
            break
        else:
            print("Print enter a valid short code to access the services")

if __name__ == '__main__':
    locker() 