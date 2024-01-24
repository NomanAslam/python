from rest_framework.test import APITestCase
from authentication.models import User, CustomUserManager

class TestModel(APITestCase):

    def test_creates_user(self):
        #self.assertEqual(1,1-0)
        user = User.objects.create_user('abc@gmail.com', 'password123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'abc@gmail.com')

    #Email
    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, email = '', password = 'password123')
        
    def test_raises_error_with_message_when_no_email_is_supplied(self):    
        with self.assertRaisesMessage(ValueError, 'Email should be provided'):
            User.objects.create_user(email = '', password ='password123')

    #password
    def test_raises_error_when_no_password_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, email = 'email', password = '')
        
    def test_raises_error_with_message_when_no_password_is_supplied(self):    
        with self.assertRaisesMessage(ValueError, 'Password should be provided'):
            User.objects.create_user(email = 'email', password ='')

    #SuperUser
    def test_creates_super_user(self):
        #self.assertEqual(1,1-0)
        user = User.objects.create_superuser('abc@gmail.com', 'password123')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'abc@gmail.com')

    def test_creates_super_user_with_is_staff_status(self):    
        with self.assertRaisesMessage(ValueError, 'Superuser should have is_staff True'):
            User.objects.create_superuser(email = '', password ='password123', is_staff = False)

    def test_creates_super_user_with_is_superuser_status(self):    
        with self.assertRaisesMessage(ValueError, 'Superuser should have is_superuser True'):
            User.objects.create_superuser(email = '', password ='password123', is_superuser = False)

    def test_creates_super_user_with_is_active_status(self):    
        with self.assertRaisesMessage(ValueError, 'Superuser should have is_active True'):
            User.objects.create_superuser(email = '', password ='password123', is_active = False)