from django.shortcuts import render,HttpResponse
from celery_app.tasks import test_func


# def test_email(request):
#     test_func.delay()
#     return HttpResponse("DONE")

