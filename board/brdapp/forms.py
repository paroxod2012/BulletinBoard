from django import forms
from .models import Post, User, UserResponse, OneTimeCode
from django.contrib.auth.forms import UserCreationForm
# Category

class AdForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           # 'author',
           'category',
           'title',
           'text',
       ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = [
            'author',
            'text',
            'article',
        ]


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2",)


class OneTimeForm(forms.ModelForm):
    class Meta:
        model = OneTimeCode
        fields = ['code']

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get("code")

        if not OneTimeCode.objects.filter(code=code).exists():
            raise forms.ValidationError(
                "Wrong code"
            )
        return cleaned_data
