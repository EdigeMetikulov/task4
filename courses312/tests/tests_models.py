# # from django.test import TestCase
# #
# # from courses312.models import Branch, Course, Contact, Category
# #
# #
# # class CategoryModelTest(TestCase):
# #     @classmethod
# #     def setUpTestData(cls):
# #         Category.objects.create(name="test", imgpath="none")
# #
# #     def
# #
# #
# # class AuthorModelTest(TestCase):
# #     @classmethod
# #     def setUpTestData(cls):
# #         # Set up non-modified objects used by all test methods
# #         Author.objects.create(first_name='Big', last_name='Bob')
# #
# #     def test_first_name_label(self):
# #         author = Author.objects.get(id=1)
# #         field_label = author._meta.get_field('first_name').verbose_name
# #         self.assertEqual(field_label, 'first name')
# #
# #     def test_date_of_death_label(self):
# #         author = Author.objects.get(id=1)
# #         field_label = author._meta.get_field('date_of_death').verbose_name
# #         self.assertEqual(field_label, 'died')
# #
# #     def test_first_name_max_length(self):
# #         author = Author.objects.get(id=1)
# #         max_length = author._meta.get_field('first_name').max_length
# #         self.assertEqual(max_length, 100)
# #
# #     def test_object_name_is_last_name_comma_first_name(self):
# #         author = Author.objects.get(id=1)
# #         expected_object_name = f'{author.last_name}, {author.first_name}'
# #         self.assertEqual(str(author), expected_object_name)
# #
# #     def test_get_absolute_url(self):
# #         author = Author.objects.get(id=1)
# #         # This will also fail if the urlconf is not defined.
# #         self.assertEqual(author.get_absolute_url(), '/catalog/author/1')
#
# from rest_framework.test import APITestCase
# from courses312.models import *
# from django.test import Client
#
# client = Client()
#
#
# class CoursesModelTesting(APITestCase):
#
#     def setUp(self):
#         self.category = category = Category.objects.create(
#             name='IT Courses',
#             imgpath='media/media/Downloader.la-6113f19a51f56.jpg'
#         )
#         self.course = Course.objects.create(
#             name='Neobis',
#             description='A young, ambitious organization that aims '
#                         'to develop Kyrgyzstan in the field of information '
#                         'technology, innovation and education',
#             category=category,
#             logo='media/media/Downloader.la-6113f5468a94c.jpg'
#         )
#         contacts = []
#
#         self.contact = Contact.objects.create(type="phone", value="9999999")
#         contacts.append(self.contact)
#
#         branches = []
#         self.branch = Branch.objects.create(latitude='42.871620',
#                                             longitude='74.608629',
#                                             address='Tynystanova, 98')
#         branches.append(self.branch)
#         self.course.contacts.add(*contacts)
#         self.course.branches.add(*branches)
#
#     def test_for_str(self):
#         category = self.category
#         branch = self.branch
#         contact = self.contact
#         course = self.course
#
#         self.assertEqual(str(category), category.name)
#         self.assertEqual(str(branch), branch.address)
#         self.assertEqual(str(contact), contact.type, contact.value)
#         self.assertEqual(str(course), course.name)
