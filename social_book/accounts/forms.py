from django import forms
from django.contrib.auth import get_user_model
from .models import UploadedFiles


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        User = get_user_model()
        model = User
        fields = ['email', 'username','password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        User = get_user_model()
        model = User
        fields = ['username', 'password']
    

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFiles
        fields = ['title', 'description','cost','year_of_published','file','Visibility']

    def clean_file(self):
        file = self.cleaned_data.get('file') #instace of uploadfile
        if not file.name.lower().endswith(('.pdf','.jpeg','.jpg')):
            raise forms.ValidationError('only pdf and jpg files are allowed.')
        return file
    
