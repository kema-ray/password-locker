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


if __name__=='__main__':
    unittest.main()