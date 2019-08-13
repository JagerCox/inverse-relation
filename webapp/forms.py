from .models import Contact
from django.forms import Textarea
from django.forms import ModelForm
from django.forms import TextInput
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = [f.name for f in Contact._meta.fields]
