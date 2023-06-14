from django.test import TestCase
from pract_app.models import account_profile

# Create your tests here.
class account_test(TestCase):
    def setup(self):
        print("setup activity")
        account_profile.objects.create(id_user=100,username='Nanda',location='Bangalore')
        account_profile.objects.create(id_user=200,username='Gopan',location='Chennai')

    def test_status(self):
        print('testing account informatiom')
        win=account_profile.objects.all()
        self.assertEqual(win.count(), 2)
        id1= account_profile.objects.get(username='Nanda')
        id2= account_profile.objects.get(username='Gopan')
        self.assertEqual(id1.get_location(), 'Bangalore')
        self.assertEqual(id2.get_location(), 'Chennai')
