from time import sleep
from django.db.models.signals import *
from django.dispatch import receiver
from django.core.mail import send_mail
from django.core.signals import *
from .models import Post, User, UserResponse
from .views import *
from django.template.loader import *


@receiver(post_save, sender=Post)
def new_post(sender, instance, created, **kwargs):
    if created:
        post_author = instance.user
        subject = f'{post_author}'
        post_title = instance.title
        post_category = instance.category
        # post_author_email = instance.article.user.email

        send_mail(
            subject=subject,
            message=f"Greetings, \n"
                    f"There's a new post in category: {instance.category} \n"
                    f"http://127.0.0.1:8000/board/{instance.id}",
            from_email='ksenia.ivanichkina@yandex.ru',
            recipient_list=[User.objects.all().values("email")])

        return redirect('/board/')


