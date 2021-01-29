from django import forms
from issue.models import Issue
from issue.utils import StatusIssue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'status', 'user']


class ChangeStatusForm(forms.Form):
    status_form = forms.ChoiceField(choices=StatusIssue)
