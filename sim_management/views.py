from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db import models
from .models import SimCard

class SimCardListView(ListView):
    model = SimCard
    template_name = 'sim_management/simcard_list.html'
    context_object_name = 'simcards'
    paginate_by = 20
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                models.Q(phone_number__icontains=query) |
                models.Q(iccid__icontains=query) |
                models.Q(owner_name__icontains=query)
            )
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        operator = self.request.GET.get('operator')
        if operator:
            queryset = queryset.filter(operator__id=operator)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = SimCard.STATUS_CHOICES
        return context

class SimCardDetailView(DetailView):
    model = SimCard
    template_name = 'sim_management/simcard_detail.html'
    context_object_name = 'simcard'