from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView


class ContactCreateView(CreateView):
    model = Contact
    success_url = reverse_lazy('success-url')
    form_class = ContactForm


class SuccessTemplateView(TemplateView):
    template_name = "webapp/success.html"


class err404View(TemplateView):
    template_name = "webapp/err404.html"


class err500View(TemplateView):
    template_name = "webapp/err500.html"
