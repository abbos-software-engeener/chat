from django.http import HttpResponse
from .tasks import test_func
from email_send.task import send_mail_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
import random

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def test_email(request):
    send_mail_task.delay()
    return HttpResponse('Sent')


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=1, minute=24)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_" + "99", task='email_send.task.send_mail_task', args=json.dumps(([2, 3])))
    return HttpResponse("Done")
