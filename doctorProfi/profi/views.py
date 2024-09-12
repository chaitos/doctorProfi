from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from .models import Appointment, Doctors
from django.http import JsonResponse



def index(request):
    #t = render_to_string('profi/index.html')
    #return HttpResponse(t)
    doctors = Doctors.objects.filter(available=True)
    data = {'title' : "Доктор Профи"}
    return render(request, 'profi/index.html', {'doctors': doctors, 'data' : data})


def price(request):
    return render(request, 'profi/prices.html', {'title' : "Цены"})


def schedule(request):
    # Получаем всех врачей из базы данных
    doctors = Doctors.objects.filter(available=True)    #проверка, доступен ли доктор
    for doctor in doctors:
        doctor.schedule_lines = doctor.work_schedule.split(',')
    # Передаем данные врачей в шаблон
    return render(request, 'profi/schedule.html', {'doctors': doctors, 'title' : "График"})


def create_appointment(request):
    doctors = Doctors.objects.filter(available=True)

    if request.method == 'POST':

        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        doctor_id = request.POST['doctor']
        message = request.POST.get('message', '')

        doctor = get_object_or_404(Doctors, id=doctor_id)
        # Создание записи
        Appointment.objects.create(
            name=name,
            phone=phone,
            email=email,
            date=date,
            time=time,
            message=message,
            doctor=doctor
        )

        # Возвращаем успешный JSON-ответ
        return JsonResponse({'success': True, 'message': 'Запись успешно создана!'})


    return render(request, 'appointment_form.html', {'doctors': doctors})

def blog(request):
    return render(request, 'profi/blog.html', {'title': "Блог"})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена :(</h1>")



