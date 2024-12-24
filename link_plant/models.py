from django.db import models

# Profiles -> LinkProfile

class Profile(models.Model):
  BG_CHOICES = (
    ('blue', 'Blue'),
    ('gree', 'Green'),
    ('yellow', 'Yellow'),
  )

  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100)
  bg_color = models.CharField(max_length=50, choices=BG_CHOICES)
  
  def __str__(self):
    return self.name
  

class LinkPlant(models.Model):
  text = models.CharField(max_length=100)
  url = models.URLField()
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")

  def __str__(self):
    return f"{self.text} | {self.url}"
