from django import forms
from .models import mfforms


class showforms(forms.ModelForm):
    name = forms.CharField(max_length=50, min_length=2)

    class Meta:
        model = mfforms
        fields = ['name', 'Email', 'Address']
        help_texts = {'name': 'Some useful help text.'}

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data["name"]

        if valname == "gaurav":
            raise forms.ValidationError("hey it is not a valid name")


# class showforms2(ModelForm):
#     name = CharField(max_length=50, min_length=2)

#     class Meta:
#         model = mfforms
#         fields = ["name", "catagory", "village"]
#         labels = {"name": "Myname", "catagory": "Email", "village": "MyDoc"}
#         help_texts = {'name': 'Some useful help text.'}
#         error_messages = {"name": {"required": "hey it will not null"},
#                           "catagory": {"required": "hey please fill this field"}
#                           }
