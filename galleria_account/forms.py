from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class LogInForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )

    '''
    this method check the email registered or not
    '''

    def clean_user_name(self):
        email = self.cleaned_data.get('user_name')
        is_exist_email = User.objects.filter(email=email).exists()
        if not is_exist_email:
            raise forms.ValidationError('This email does not register')
        else:
            return email


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        validators=[validate_password]
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password', 'class': 'form-control'})
    )

    '''
        this method check the email registered or not
        '''

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('This email has been registered')
        else:
            return email

    '''
        this method check the passwords are match
        '''

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('re_password')
        if password != password_2:
            raise forms.ValidationError('Passwords does not match')
        else:
            return password


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-control'})
    )


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter current password', 'class': 'form-control'}),
        label='Current Password'
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter new Password', 'class': 'form-control'}),
        label='New Password'
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter new password', 'class': 'form-control'}),
        label='Confirm New Password'
    )

    class Meta:
        Model = User
        fields = ('old_password', 'new_password1', 'new_password2')
