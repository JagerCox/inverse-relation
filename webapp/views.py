from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Contact
from .forms import ContactForm
from django.urls import reverse, reverse_lazy


class ContactCreateView(CreateView):
    model = Contact
    success_url = reverse_lazy('success-url')
    # fields = ["name", "surname", "nick_name", "alias", "place", "birth_date", "phone_number_one", "phone_number_two",
    #           "phone_number_three", "email_one", "email_two", "email_three", "email_four", "telegram_user",
    #           "github_user", "bitbucket_user", "facebook_user", "pinteres_user", "twitter_user", "additional_data"]
    form_class = ContactForm

class SuccessTemplateView(TemplateView):
    template_name = "webapp/thanks.html"


class err404View(TemplateView):
    template_name = "webapp/err404.html"


class err500View(TemplateView):
    template_name = "webapp/err500.html"