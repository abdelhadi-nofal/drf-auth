from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Car

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_car = Car.objects.create(
            driver = test_user,
            car_type = 'Mazda',
            car_disc = 'It is japan'
        )
        test_car.save()

    def test_blog_content(self):
        car = Car.objects.get(id=1)
        actual_driver = str(car.driver)
        actual_car_type = str(car.car_type)
        actual_car_disc = str(car.car_disc)
        self.assertEqual(actual_driver, 'testuser')
        self.assertEqual(actual_car_type, 'Mazda')
        self.assertEqual(actual_car_disc, 'It is japan')