from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    name = models.CharField(max_length=25, help_text="Example: John", null=False, blank=False)
    surname = models.CharField(max_length=100, help_text="Example: Doe", null=False, blank=False)
    nick_name = models.CharField(max_length=25, help_text="Example: J4Nthng", null=True, blank=True)
    alias = models.CharField(max_length=25, help_text="Example: Jonny", null=True, blank=True)
    place = models.CharField(max_length=512,  help_text="Example: We kwonw two years ago in a congress about...",
                             null=False, blank=False)
    birth_date = models.DateField(help_text="Format YYYY/MM/DD  Ex: 2018/06/30", null=True, blank=True)

    phone_number_one = PhoneNumberField(help_text="Example: +34611111111", null=False, blank=False)
    phone_number_two = PhoneNumberField(help_text="Example: +34622222222", null=True, blank=True)
    phone_number_three = PhoneNumberField(help_text="Example: +34633333333", null=True, blank=True)

    email_one = models.EmailField(help_text="Example: johndoe@mail.com", null=True, blank=True)
    email_two = models.EmailField(help_text="Example: johndoe@yahoo.com", null=True,
                                    blank=True)
    email_three = models.EmailField(help_text="Example: johndoe@gmail.com", null=True,
                                    blank=True)
    email_four = models.EmailField(help_text="Example: johndoe@proton.com", null=True,
                                    blank=True)

    telegram_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: @johndoe")
    github_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: johndoe")
    bitbucket_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: johndoe")
    facebook_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: johndoe")
    pinteres_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: johndoe")
    twitter_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: @johndoe")

    additional_data = models.CharField(max_length=100, null=True, blank=True, help_text="Example: Doe")

    def __str__(self):
        return 'Name/Surname/Nick({}/{}/{})'.format(self.name, self.surname, self.nick_name)
