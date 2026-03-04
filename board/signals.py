from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Response

@receiver(post_save, sender=Response)
def notify_post_author(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Новый отклик на ваше объявление',
            message=f'Пользователь {instance.author.username} оставил отклик: {instance.text}',
            from_email=None,
            recipient_list=[instance.post.author.email],
        )
    elif instance.status:
        send_mail(
            subject='Ваш отклик принят!',
            message=f'Автор объявления "{instance.post.title}" принял ваш отклик.',
            from_email=None,
            recipient_list=[instance.author.email],
        )