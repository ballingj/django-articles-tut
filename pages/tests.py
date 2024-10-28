from django.test import SimpleTestCase, TestCase
from django.urls import reverse  # new


class PagesTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/pages/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  # new
        response = self.client.get(reverse("pages"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("pages"))
        self.assertTemplateUsed(response, "pages/home.html")
    
    def test_template_content(self): # new
        response = self.client.get(reverse("pages"))
        self.assertContains(response, "<h1>Pages</h1>")


class AboutPageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/pages/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  # new
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")
    
    def test_template_content(self): # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")
