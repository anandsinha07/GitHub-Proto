from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Cannot use this username. It's already registered.")
        return username


    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Cannot use this email. It's already registered.")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            # print(user.profile)
            # user.profile.send_activation_email() # celery delay
        return user

class EditProfileForm(forms.ModelForm):
    """A form for updating user profiles. Includes all the required
    fields"""
    company = forms.CharField(label='company', max_length=120)
    education = forms.CharField(label='education', max_length=120)
    description = forms.CharField(label='description')

    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'last_name')

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(EditProfileForm, self).__init__(*args, **kwargs)


    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username == self.user.username:
            pass
        else:
            qs = User.objects.filter(username__iexact=username)
            if qs.exists():
                raise forms.ValidationError("Cannot use this username. It's already registered.")
        return username


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email == self.user.email:
            pass
        else:
            qs = User.objects.filter(email__iexact=email)
            if qs.exists():
                raise forms.ValidationError("Cannot use this email. It's already registered.")
        return email

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(EditProfileForm, self).save(commit=False)
        if commit:
            user.save()
            profile = user.profile
            profile.company = self.cleaned_data.get("company")
            profile.education = self.cleaned_data.get("education")
            profile.description = self.cleaned_data.get("description")
            profile.save()
        return user
