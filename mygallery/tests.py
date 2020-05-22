from django.test import TestCase
from .models import ImagePost, ImageLocation, ImageCategory
# Create your tests here.


class TestImagePost(TestCase):

    def setUp(self):
        self.new_category = ImageCategory(name='nature')
        self.new_category.save_imagecategory()

        self.new_location = ImageLocation(name="Aboretum")
        self.new_location.save_imagelocation()

        self.new_image = ImagePost(image_name='hacker', image_description='This guy is a real hacker',
                               image_location=self.new_location, image_category=self.new_category)
        self.new_image.save_imagepost()

    def test_isinstance(self):
        self.new_image = ImagePost(image_name='hacker', image_description='This guy is a real hacker', 
                               image_location=self.new_location,image_category=self.new_category)
        self.new_image.save_imagepost()
        self.assertTrue(isinstance(self.new_image, ImagePost))