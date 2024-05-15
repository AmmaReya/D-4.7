#from django.contrib.auth.models import User
#from django.core.mail import EmailMultiAlternatives
#from django.db.models.signals import m2m_changed
#from django.dispatch import receiver
#
#from .models import PostCategory
#
#
#@receiver(m2m_changed, sender=PostCategory)
#def post_created(instance, sender, **kwargs):
#    if kwargs['action'] == 'post_add':
#        subscribers_email = []
#        for category in instance.post_category.all():
#            subscribers_email += User.objects.filter(subscriptions__category=category).values_list('email', flat=True)
#            subject = f'Новый пост в твоей любимой категории'
#            text_content = (
#                f'Пост: {instance.title}\n'
#                f'Автор: {instance.author.author.username}\n\n'
#                f'Читать больше: http://127.0.0.1:8000{instance.get_absolute_url()}'
#            )
#            html_content = (
#                f'Пост: {instance.title}<br>'
#                f'Автор: {instance.author.author.username}<br><br>'
#                f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
#                f'Читать больше </a>'
#            )
#            for email in subscribers_email:
#                msg = EmailMultiAlternatives(subject, text_content, None, [email])
#                msg.attach_alternative(html_content, 'text/html')
#                msg.send()
