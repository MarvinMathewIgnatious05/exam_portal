from django import forms
from .models import MockTestSubmission

class MockTestSubmissionForm(forms.ModelForm):
    class Meta:
        Model = MockTestSubmission
        Fields = ['mocktest', 'total_attended', 'unattended', 'score']



