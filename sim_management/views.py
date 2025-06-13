from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db import models
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SimCard, ExternalBot
from .serializers import SimCardSerializer, ExternalBotSerializer
from .tasks import send_command_to_bot

def sim_card_list(request):
    """
    Отображает список SIM-карт с поиском, фильтрами и пагинацией.
    """
    queryset = SimCard.objects.all().order_by('id')  # Сортировка для устранения UnorderedObjectListWarning

    # Поиск
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            models.Q(phone_number__icontains=query) |
            models.Q(iccid__icontains=query)
        )

    # Фильтры
    status = request.GET.get('status')
    if status:
        queryset = queryset.filter(status=status)

    # Пагинация
    paginator = Paginator(queryset, 10)  # 10 SIM-карт на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Выбор статуса для фильтра
    status_choices = SimCard._meta.get_field('status').choices

    context = {
        'simcards': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'status_choices': status_choices,
        'request': request,
    }
    return render(request, 'sim_management/simcard_list.html', context)

def sim_card_detail(request, pk):
    """
    Отображает детальную информацию о SIM-карте.
    """
    simcard = get_object_or_404(SimCard, pk=pk)
    return render(request, 'sim_management/simcard_detail.html', {'simcard': simcard})

class SimCardViewSet(viewsets.ModelViewSet):
    queryset = SimCard.objects.all()
    serializer_class = SimCardSerializer
    permission_classes = [IsAuthenticated]

class ExternalBotViewSet(viewsets.ModelViewSet):
    queryset = ExternalBot.objects.all()
    serializer_class = ExternalBotSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def send_command(self, request, pk=None):
        bot = self.get_object()
        command = request.data.get('command')
        params = request.data.get('params', {})
        if not command:
            return Response({'error': 'Command is required'}, status=400)
        task = send_command_to_bot.delay(bot.id, command, params)
        return Response({'task_id': task.id, 'status': 'Command sent to Celery'})