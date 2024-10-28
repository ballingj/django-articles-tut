from django import forms
from app.models import Article


class CreateArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ("title", "status", "content", "word_count", "twitter_post")

