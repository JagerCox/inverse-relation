from django.forms import ModelForm
from django.forms import TextInput
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "surname", "nick_name", "alias", "place", "birth_date", "phone_number_one",
                  "phone_number_two", "phone_number_three", "email_one", "email_two", "email_three", "email_four",
                  "telegram_user", "github_user", "bitbucket_user", "facebook_user", "pinteres_user", "twitter_user",
                  "additional_data")
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'nick_name': TextInput(attrs={'class': 'form-control'}),
            'alias': TextInput(attrs={'class': 'form-control'}),
            'place': TextInput(attrs={'class': 'form-control'}),
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
            'pinteres_user': TextInput(attrs={'class': 'form-control'}),
            'twitter_user': TextInput(attrs={'class': 'form-control'}),
            'additional_data': TextInput(attrs={'class': 'form-control'})
        }
        #
        # name = models.CharField(max_length=25, help_text="Example: John", null=False, blank=False)
        # surname = models.CharField(max_length=100, help_text="Example: Doe", null=False, blank=False)
        # nick_name = models.CharField(max_length=25, help_text="Example: J4Nthng", null=True, blank=True)
        # alias = models.CharField(max_length=25, help_text="Example: Jonny", null=True, blank=True)
        # place = models.CharField(max_length=512, help_text="Example: We kwonw two years ago in a congress about...",
        #                          null=False, blank=False)
        # birth_date = models.DateField(help_text="Format YYYY/MM/DD  Ex: 2018/06/30", null=True, blank=True)
        #
        # phone_number_one = PhoneNumberField(help_text="Example: +34611111111", null=False, blank=False)
        # phone_number_two = PhoneNumberField(help_text="Example: +34622222222", null=True, blank=True)
        # phone_number_three = PhoneNumberField(help_text="Example: +34633333333", null=True, blank=True)
        #
        # email_one = models.EmailField(help_text="Example: johndoe@mail.com", null=True, blank=True)
        # email_two = models.EmailField(help_text="Example: johndoe@yahoo.com", null=True,
        #                               blank=True)
        # email_three = models.EmailField(help_text="Example: johndoe@gmail.com", null=True,
        #                                 blank=True)
        # email_four = models.EmailField(help_text="Example: johndoe@proton.com", null=True,
        #                                blank=True)
        #
        # telegram_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: @johndoe")
        # github_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: johndoe")
        # bitbucket_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: johndoe")
        # facebook_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: johndoe")
        # pinteres_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: johndoe")
        # twitter_user = models.CharField(max_length=30, null=True, blank=True, help_text="Example: @johndoe")
        #
        # additional_data = models.CharField(max_length=100, null=True, blank=True, help_text="Example: Doe")