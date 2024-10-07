from django.test import TestCase
from ..models import Country, Manufacturers, Cars, Comments
from django.core.exceptions import ValidationError

class CountryModelTest(TestCase):
    def test_create_country(self):
        country = Country.objects.create(name="Россия")
        self.assertEqual(country.name, "Россия")

class ManufacturersModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Россия")

    def test_create_manufacturer(self):
        manufacturer = Manufacturers.objects.create(name="АвтоВАЗ", country=self.country)
        self.assertEqual(manufacturer.name, "АвтоВАЗ")
        self.assertEqual(manufacturer.country, self.country)

class CarsModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Россия")
        self.manufacturer = Manufacturers.objects.create(name="АвтоВАЗ", country=self.country)

    def test_create_car(self):
        car = Cars.objects.create(name="Лада Гранта", manufacturer=self.manufacturer, start_year="2011-01-01")
        self.assertEqual(car.name, "Лада Гранта")
        self.assertEqual(car.manufacturer, self.manufacturer)
        self.assertEqual(car.start_year, "2011-01-01")
        self.assertIsNone(car.end_year)

class CommentsModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Россия")
        self.manufacturer = Manufacturers.objects.create(name="АвтоВАЗ", country=self.country)
        self.car = Cars.objects.create(name="Лада Гранта", manufacturer=self.manufacturer, start_year="2011-01-01")

    def test_create_comment(self):
        comment = Comments.objects.create(email_autor="user@example.com", car=self.car, comment="Отличный автомобиль!")
        self.assertEqual(comment.email_autor, "user@example.com")
        self.assertEqual(comment.car, self.car)
        self.assertEqual(comment.comment, "Отличный автомобиль!")

    def test_invalid_email(self):
        with self.assertRaises(ValidationError):
            comment = Comments(email_autor="invalid_email", car=self.car, comment="Некорректный email")
            comment.full_clean()

    def test_str_method(self):
        comment = Comments.objects.create(email_autor="user@example.com", car=self.car, comment="Отличный автомобиль!")
        self.assertEqual(str(comment), "комментарий user@example.com о Лада Гранта")