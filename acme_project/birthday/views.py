from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView, ListView,  DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .utils import calculate_birthday_countdown

from .forms import BirthdayForm

from .models import Birthday

class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context 