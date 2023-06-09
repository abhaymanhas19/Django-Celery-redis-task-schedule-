from celery import shared_task
from django.core.mail import send_mail
from django_celery import settings


@shared_task(bind=True)
def test_func(self):
   mail_subject=" hi scfsdafcsdcfsdcfsdcsdcxcxthis is a test mailing "
   message=" Hi  welcome cscscscdxscdscsc ccccccccccccccccccccccccccccccccccto our site. this is a confirmation "
   to_email="manhasabhay000@gmail.com"
   try:
      send_mail(subject=mail_subject,
             message=message,
             from_email=settings.EMAIL_HOST_USER,
             recipient_list=[to_email],
             fail_silently=True,
            )
   except Exception as e :
      print(e)
   return "Email send by celery"