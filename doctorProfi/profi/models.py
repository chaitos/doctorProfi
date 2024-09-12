from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя пациента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронная почта")
    date = models.DateField(verbose_name="Дата приёма")
    time = models.TimeField(verbose_name="Время приёма")
    message = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    doctor = models.ForeignKey('Doctors', on_delete=models.CASCADE, verbose_name="Врач", null=True, default=1)

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

    class Meta:
        verbose_name = "Запись на посещение"
        verbose_name_plural = "Записи на посещения"

class Doctors(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя врача")
    specialization = models.CharField(max_length=100, verbose_name="Специализация")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    work_schedule = models.CharField(max_length=255, verbose_name="График работы")
    email = models.EmailField(verbose_name="Электронная почта")
    available = models.BooleanField(default=True, verbose_name="Принимает пациентов")

    def __str__(self):
        return f'{self.name} - {self.specialization}'

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"