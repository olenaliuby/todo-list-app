from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo_app.forms import TaskCreateForm, TaskContentSearchForm
from todo_app.models import Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo_app/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        content = self.request.GET.get("content", "")

        context["search_form"] = TaskContentSearchForm(
            initial={"content": content}
        )
        return context

    def get_queryset(self):
        form = TaskContentSearchForm(self.request.GET)
        if form.is_valid():
            return super().get_queryset().filter(
                content__icontains=form.cleaned_data["content"]
            )


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo-app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo-app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo-app:index")


class TaskCompleteUpdateView(View):
    @staticmethod
    def post(request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo-app:index")
