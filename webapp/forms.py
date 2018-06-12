from .models import Contact
from django.forms import Textarea
from django.forms import ModelForm
from django.forms import TextInput
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ("name", "surname", "nick_name", "alias", "place", "birth_date", "phone_number_one",
                  "phone_number_two", "phone_number_three", "email_one", "email_two", "email_three", "email_four",
                  "telegram_user", "github_user", "bitbucket_user", "facebook_user", "pinterest_user", "twitter_user",
                  "additional_data")
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'nick_name': TextInput(attrs={'class': 'form-control'}),
            'alias': TextInput(attrs={'class': 'form-control'}),
            'place': Textarea(attrs={'class': 'form-control'}),
            'birth_date': TextInput(attrs={'class': 'form-control'}),
            'phone_number_one': TextInput(attrs={'class': 'form-control'}),
            'phone_number_two': TextInput(attrs={'class': 'form-control'}),
            'phone_number_three': TextInput(attrs={'class': 'form-control'}),
            'email_one': TextInput(attrs={'class': 'form-control'}),
            'email_two': TextInput(attrs={'class': 'form-control'}),
            'email_three': TextInput(attrs={'class': 'form-control'}),
            'email_four': TextInput(attrs={'class': 'form-control'}),
            'telegram_user': TextInput(attrs={'class': 'form-control'}),
            'github_user': TextInput(attrs={'class': 'form-control'}),
            'bitbucket_user': TextInput(attrs={'class': 'form-control'}),
            'facebook_user': TextInput(attrs={'class': 'form-control'}),
            'pinterest_user': TextInput(attrs={'class': 'form-control'}),
            'twitter_user': TextInput(attrs={'class': 'form-control'}),
            'additional_data': Textarea(attrs={'class': 'form-control'})
        }
