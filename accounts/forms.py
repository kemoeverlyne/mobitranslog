from django import forms
from django.core.exceptions import ValidationError
from .models import User,Department

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    departments = forms.ModelMultipleChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))



    class Meta:
        model = User
        fields = ['name', 'email','departments' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
        

    def clean_name(self):
        name = self.cleaned_data['name']
        if User.objects.filter(name=name).exists():
            raise ValidationError('A user with this name already exists.')
        return name

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise ValidationError("Passwords do not match.")

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'password']

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError('A user with this email does not exist')
        return email
