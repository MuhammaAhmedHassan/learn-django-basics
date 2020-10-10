from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta: # inside this class where we define how we want
        # to output our form, which fields do we want to be present
        # and from which model do we want to inherit these fields from
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']
