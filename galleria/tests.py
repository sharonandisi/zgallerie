from django.test import TestCase
from .models import Blogger,Photo,tags

# Create your tests here.
class BloggerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.sharon= Blogger(first_name = 'Sharon', last_name ='Andisi', email ='sharonandisi.sa@gmail.com')
        self.sharon.save_blogger()
        #creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_photos= Photo(title = 'Test Photo',post='This is a random test Post',editor = self.sharon)
        self.new_photo.save()

        self.new_photo.tags.add(self.new_tag)
    def test_instance(self):
        self.assertTrue(isinstance(self.sharon,Blogger))
    def test_save_method(self):
        self.sharon.save_blogger()
        bloggers = Blogger.objects.all()
        self.assertTrue(len(bloggers) > 0)
    def tearDown(self):
        Blogger.objects.all().delete()
        tags.objects.all().delete()
        Photo.objects.all().delete()
    def test_get_photos_of_the_day(self):
        photos_galleria = Article.todays_photos()
        self.assertTrue(len(today_photos)>0)