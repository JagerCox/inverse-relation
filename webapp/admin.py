from .models import Contact
from django.contrib import admin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "nick_name", "alias", "place", "birth_date", "phone_number_one",
                    "phone_number_two", "phone_number_three", "email_one", "email_two", "email_three", "email_four",
                    "telegram_user", "github_user", "bitbucket_user", "facebook_user", "pinteres_user", "twitter_user",
                    "additional_data"]
