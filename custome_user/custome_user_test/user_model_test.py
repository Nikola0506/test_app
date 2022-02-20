from django.test import TestCase

from custome_user.models import CustomeUsers


class TestModelUser(TestCase):

    @classmethod
    def setUp(cls):
        # create test user
        cls.user = CustomeUsers.objects.create_user(
            ime='tet_nikola',
            prezime='test_aleksic',
            username='test_username',
            password='test',
            email='test@example.com'
        )

    def test_queryset_exists(self):
        qs = CustomeUsers.objects.all()
        self.assertTrue(qs.exists())

    def test_id_korisnika_exist(self):
        # user id
        user_id = self.CustomeUsers.id
        print('user id in test database: ' + str(user_id))
        print('---------------')
        self.assertEqual(1, user_id)

    def test_ime_korisnika_exist(self):
        # user name
        user_name = self.CustomeUsers.first_name
        print('user name in database: ' + str(user_name))
        print('---------------')
        self.assertEqual('test_nikola', user_name)

    def test_prezime_korisnika_exist(self):
        # user last name
        last_name = self.CustomeUsers.last_name
        print('last name in database: ' + str(last_name))
        print('---------------')
        self.assertEqual('test_last_name', last_name)
