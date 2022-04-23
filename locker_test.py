from cgi import test
import unittest
from locker import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviors
    '''
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_user = User("RachelOyondi","kema99Ray")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"RachelOyondi")
        self.assertEqual(self.new_user.password,"kema99Ray")

    def test_save_user(self):
        '''
        test_save_user teat case to test if the user object is saved into
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run.
        '''
        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","qwerty2u")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_all_users(self):
        '''
        A method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Test","qwerty2u")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

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

if __name__=='__main__':
    unittest.main()