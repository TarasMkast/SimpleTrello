from django.shortcuts import render, redirect
from issue.forms import IssueForm, ChangeStatusForm
from issue.models import Issue


def catalog_issue(request, pk):
    return render(request, 'issue/issue_list.html', {'issue_list': Issue.objects.filter(project=pk)})


def create_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
    form = IssueForm()
    return render(request, 'registration/verify.html', {'form_create': form})


def change_status_issue(request, pk):
    if request.method == 'POST':
        form = IssueForm(request)
        if form.is_valid():
            issue = Issue.objects.get(id=pk)
            issue.status = form
            issue.save()
            return redirect('project')
    form = ChangeStatusForm()
    return render(request, 'issue/issue_status.html', {'form_status': form})
