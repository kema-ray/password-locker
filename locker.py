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
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list