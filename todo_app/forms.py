from django import forms
from django.forms import DateTimeInput
from django.utils import timezone

from todo_app.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=DateTimeInput(
            attrs={"type": "datetime-local"}),
        initial=timezone.now().replace(second=0, microsecond=0)
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskContentSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by content"})
    )
