from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creating a new user with an email is succeful"""

        email = 'testUser@test.com'
        password = 'Pass1234'

        user = get_user_model().objects\
            .create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email of a new user is stored normilized"""

        email = 'testuser@GMAIL.COM'

        user = get_user_model().objects.create_user(email, '1234Abcd')

        self.assertEqual(user.email, email.lower())

    def test_invalid_user_email(self):
        """Test that when trying to create a new user
            with invalid email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'asd')

    def test_create_super_user(self):
        """Test creating a super user"""

        user = get_user_model().objects.create_superuser(
            'fakemail@hotmail.com', 'Pppp3154'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
