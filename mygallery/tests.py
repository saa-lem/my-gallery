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

    def test_save_imagepost(self):
        images = ImagePost.objects.all()
        self.assertTrue(len(images)>0)

         def test_delete_imagepost(self):
      
        self.new_image.delete_imagepost()
        images = ImagePost.objects.all()
        self.assertTrue(len(images)==0)

    def test_get_image_by_id(self):
        image = ImagePost.get_image_by_id(id=2)
        self.assertTrue(self.new_image == image)

    def test_search_image(cls):
        images = ImagePost.search_image('nature')
        cls.assertTrue(len(images)==1)

    def test_search_by_location(cls):
        images = ImagePost.search_by_location('Aboretum')
        cls.assertTrue(len(images)==1)
        




    def tearDown(self):
        ImageLocation.objects.all().delete()
        ImageCategory.objects.all().delete()
        ImagePost.objects.all().delete()   