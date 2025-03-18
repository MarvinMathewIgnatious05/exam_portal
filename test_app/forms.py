from django import forms
from .models import MockTestSubmission, PracticalTestSubmission

class MockTestSubmissionForm(forms.ModelForm):
    class Meta:
        Model = MockTestSubmission
        Fields = ['mocktest', 'total_attended', 'unattended', 'score']

class PracticalTestSubmissionForm(forms.ModelForm):

    class Meta:
        Model = PracticalTestSubmission
        Fields = '__all__'





