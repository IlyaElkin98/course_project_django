from django import forms
from newsletter.models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ["start_time", "end_time", "message", "recipients"]
