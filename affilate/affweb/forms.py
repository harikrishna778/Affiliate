from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from affweb.models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class SignInForm(AuthenticationForm):
    pass
