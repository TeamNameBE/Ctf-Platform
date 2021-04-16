import django.forms as forms
from ctf.models import Challenge


class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ["name", "points", "description", "category", "pad"]
