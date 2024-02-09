from django.contrib.auth.forms import UserCreationForm
from . models import User,Feedback
from django import forms


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'location', 'phone_no', 'profile_image']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'


