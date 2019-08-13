from django.contrib import admin
from django.urls import path
from webapp.views import ContactCreateView, SuccessTemplateView, err404View, err500View, download_vcard, counter_contacts
from django.urls import include

urlpatterns = [
    path('', ContactCreateView.as_view(), name="create-contact"),
    path('success/', SuccessTemplateView.as_view(), name="success-url"),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
    path('download/', download_vcard),
    path('counter/', counter_contacts)
]

# With settings.DEBUG = False
handler404 = err404View.as_view()
handler500 = err500View.as_view()
