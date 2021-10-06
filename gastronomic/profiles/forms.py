from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import UserProfile

class UserCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('email',)

class UserChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('email',)
