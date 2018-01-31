from django.contrib import admin
from django.urls import path
from webapp.views import ContactCreateView, SuccessTemplateView, err404View, err500View
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ContactCreateView.as_view(), name="create-contact"),
    path('success/', SuccessTemplateView.as_view(), name="success-url"),
    path('captcha/', include('captcha.urls')),
]

# With settings.DEBUG = False
handler404 = err404View.as_view()
handler500 = err500View.as_view()
