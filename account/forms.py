from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from account.models import User


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'date_of_birth')

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_superuser')

    password = ReadOnlyPasswordHashField()

    def clean_password(self):
        return self.initial['password']
