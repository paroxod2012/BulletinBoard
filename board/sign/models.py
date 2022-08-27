from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Почта')
    first_name = forms.CharField(label = 'Представься')
    last_name = forms.CharField(label = 'Как по батюшке?')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='wanderer')
        basic_group.user_set.add(user)
        return user
