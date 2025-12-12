from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, ListView,  DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

from .utils import calculate_birthday_countdown

from .forms import BirthdayForm

from .models import Birthday

class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(LoginRequiredMixin, CreateView):
    model = Birthday
    form_class = BirthdayForm

    def form_valid(self, form):
        # Присвоить полю author объект пользователя из запроса.
        form.instance.author = self.request.user
        # Продолжить валидацию, описанную в форме.
        return super().form_valid(form) 


class BirthdayUpdateView(LoginRequiredMixin, UpdateView):
    model = Birthday
    form_class = BirthdayForm

    def dispatch(self, request, *args, **kwargs):
        # При получении объекта не указываем автора.
        # Результат сохраняем в переменную.
        instance = get_object_or_404(Birthday, pk=kwargs['pk'])
        # Сверяем автора объекта и пользователя из запроса.
        if instance.author != request.user:
            # Здесь может быть как вызов ошибки, так и редирект на нужную страницу.
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)  


class BirthdayDeleteView(LoginRequiredMixin,DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')

    def dispatch(self, request, *args, **kwargs):
        # При получении объекта не указываем автора.
        # Результат сохраняем в переменную.
        instance = get_object_or_404(Birthday, pk=kwargs['pk'])
        # Сверяем автора объекта и пользователя из запроса.
        if instance.author != request.user:
            # Здесь может быть как вызов ошибки, так и редирект на нужную страницу.
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs) 


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context 