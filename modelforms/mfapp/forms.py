from django.forms import ModelForm, PasswordInput, EmailField, TextInput, FileInput, CharField
from .models import mfforms


class showforms(ModelForm):
    name = CharField(max_length=50, min_length=2)

    class Meta:
        model = mfforms
        fields = ["name", "catagory", "village"]
        labels = {"name": "Myname", "catagory": "Email", "village": "MyDoc"}
        help_texts = {'name': 'Some useful help text.'}
        error_messages = {"name": {"required": "hey it will not null"},
                          "catagory": {"required": "hey please fill this field"}
                          }

        widgets = {
            'name': PasswordInput(attrs={'cols': 80, 'rows': 20}),
            'catagory': TextInput(attrs={"class": "myemail", "placeholder": "enter email here"}),
            'village': TextInput(attrs={"class": "myfile", "placeholder": "enter email here"})
        }
