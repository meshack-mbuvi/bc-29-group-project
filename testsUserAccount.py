import unittest
from user_views import signup, login


class testuser(unittest.TestCase):

    def setUp(self):
        self.username = 'meshack'
        self.password = 'very secret'
        self.conf_pass = 'very secret'
        self.user_category = 'user'

    def test_can_user_sign_up(self):
        """test user sign up"""
        results = signup(self.username, self.password,
                         self.conf_pass, self.user_category)
        self.assertEqual(results, 'Account created successfully')

    def test_cannot_signup_more_than_once(self):
        """test user cannot create more than one account"""
        signup(self.username, self.password,
               self.conf_pass, self.user_category)
        results = signup(self.username, self.password,
                         self.conf_pass, self.user_category)
        self.assertEqual(results, 'user already exists')

    def test_cannot_sign_up_with_unmatching_passwords(self):
        """test user cannot be signed up when passwords do not match"""
        password = 'very secret'
        conf_pass = 'not very'
        results = signup(self.username, password,
                         conf_pass, self.user_category)
        self.assertEqual(results, 'passwords provided do not match')

    def test_cannot_sign_up_with_empty_password_or_username(self):
        """test user cannot be signed up with empty password and username fields"""
        password = ''
        conf_pass = ''
        results = signup(self.username, password,
                         conf_pass, self.user_category)
        self.assertEqual(results, 'username or password cannot be empty')

    def test_user_cant_login_with_empty_password_or_username(self):
        username = ''
        password = ''

        results = login(username, password)
        self.assertEqual(results, 'username or password cannot be empty')

    def test_user_login_with_correct_details(self):
        signup(self.username, self.password,self.conf_pass, self.user_category)
        results = login(self.username, self.password)
        self.assertEqual(results, "succefully logged in as {}".format(self.username))


    
