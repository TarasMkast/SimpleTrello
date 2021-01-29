from django import forms
from issue.models import Issue, StatusIssue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'status', 'user']


class ChangeStatusForm(forms.Form):
    status_form = forms.ChoiceField(choices=StatusIssue)
