import datetime

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, Subscription
from django.conf import settings


@shared_task
def send_email_task(pk):
    post = Post.objects.get(pk=pk)
    subscribers_emails = User.objects.filter(subscriptions__category__in=post.post_category.all()).values_list('email', flat=True)
    subject = 'Новый пост в твоей любимой категории'
    text_content = (
        f'Пост: {post.title}\n'
        f'Содержание: {post.preview()}<br><br>'
        f'Читать больше: http://127.0.0.1{post.get_absolute_url()}'
    )
    html_content = (
        f'Пост: {post.title}<br>'
        f'Содержание: {post.preview()}<br><br>'
        f'<a href="http://127.0.0.1:8000{post.get_absolute_url()}">'
        f'Читать больше</a>'
    )
    for email in subscribers_emails:
        msg = EmailMultiAlternatives(subject, text_content, from_email=settings.DEFAULT_FROM_EMAIL, to=[email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


@shared_task
def weekly_send_email_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(post_time_in__gte=last_week)
    categories = set(posts.values_list('post_category__tag', flat=True))
    subscribers = set(Subscription.objects.filter(category__tag__in=categories).values_list('user__email', flat=True))

    html_content = render_to_string(
        'new_post_mail.html',
        {'link': settings.SITE_URL,
         'posts': posts}
    )
    msg = EmailMultiAlternatives(
        subject='Посты за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
