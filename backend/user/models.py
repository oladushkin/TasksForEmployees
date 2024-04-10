from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class JobTitle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должность'


class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    job_title = models.ForeignKey(
        JobTitle,
        on_delete=models.CASCADE,
        verbose_name='Должность',
        null=True
    )
    phone = models.CharField(
        max_length=50,
        verbose_name='Номер телефона'
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.employee.save()
