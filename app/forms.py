from django import forms
 

class CreateArticleForm(forms.Form):
  ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
  )
  
  title = forms.CharField(max_length=100)
  status = forms.ChoiceField(choices=ARTICLE_STATUS)
  content = forms.CharField(widget=forms.Textarea)
  word_count = forms.IntegerField()
  twitter_post = forms.CharField(widget=forms.Textarea, required=False)
