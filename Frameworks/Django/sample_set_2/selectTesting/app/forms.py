from django import forms
from .models import PostTable
from django.core.validators import RegexValidator
import re


class PostForm(forms.ModelForm):
    CATEGORY_CHOICES = (
        ('education', 'Education'),
        ('knowledge', 'Knowledge'),
        ('other', 'Other'),
    )
    category = forms.ChoiceField(choices=CATEGORY_CHOICES,widget=forms.Select(attrs={'class': 'form-control'}))
    topic=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'topic'}))
    link=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'link'}))
    def clean_topic(self):
        topic = self.cleaned_data['topic']
        # Define a regular expression pattern to match only letters
        pattern = r'^[a-zA-Z\s]+$'
        if not re.match(pattern, topic):
            raise forms.ValidationError("Topic should only contain letters and spaces.")
        return topic

    def clean_link(self):
        link = self.cleaned_data['link']

        # Define a regular expression pattern to check for the presence of <iframe> tag
        pattern = r'<iframe.*?</iframe>'

        if not re.search(pattern, link):
            raise forms.ValidationError("Link should include an <iframe> tag.")

        return link
    class Meta:
        model = PostTable
        fields = '__all__'
    
        
        
        



























    # class Meta:
    #     model = PostTable
    #     fields = '__all__'
    #    	widget={
    #    	'topic':forms.TextInput(attrs={})
    #    	'link':forms.TextInput(attrs={})
    #    	'content':forms.TextInput(attrs={})

    #    	}    