from django.test import SimpleTestCase, TestCase
from django.urls import reverse  # new


class ArticlesListTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/articles/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  # new
        response = self.client.get(reverse("articles"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("articles"))
        self.assertTemplateUsed(response, "app/home.html")
    
    def test_template_content(self): # new
        response = self.client.get(reverse("articles"))
        self.assertContains(response, "<h1>Articles</h1>")
