from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from . import models
from .models import OrganizationalMember
from django.http import JsonResponse




def base(request):
    return render(request, 'base.html')


def drevo(request):
    # Извлекаем всех сотрудников из базы данных
    info = OrganizationalMember.objects.all()  # Это извлечет все записи сотрудников
    return render(request, 'drevo.html', {'info': info})

def drevo_detail(request, info_id):
    # Получаем информацию о сотруднике по ID
    try:
        info = OrganizationalMember.objects.get(id=info_id)
        data = {
            'id': info.id,
            'name': info.name,
            'surname': info.surname,
            'position': info.position,
            'email': info.email,
            'description': info.description,
        }
        return JsonResponse(data)
    except OrganizationalMember.DoesNotExist:
        return JsonResponse({'error': 'Сотрудник не найден'}, status=404)


def search(request):
    query = request.GET.get('query', '')
    if query:
        # Фильтрация по всем ключевым полям
        employees = OrganizationalMember.objects.filter(
            Q(name__icontains=query) |
            Q(surname__icontains=query) |
            Q(position__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        employees = OrganizationalMember.objects.all()  # Если нет запроса, показываем всех сотрудников

    return render(request, 'search.html', {'employees': employees, 'query': query})

