from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Post, ChangeLog

@receiver(post_save, sender=Post)
def log_comic_created(sender, instance, created, **kwargs):
    if created:
        ChangeLog.objects.create(
            content_object = instance,
            action = 'Comic created',
        )
        print(f'[Signal] Logged creation of: {instance.title}')

@receiver(m2m_changed, sender=Post.comic_tags.through)
def log_tags_changes(sender, instance, action, **kwargs):
    if action == 'post_add':
        ChangeLog.objects.create(
            content_object = instance,
            action = 'Tags updated'
        )
        print(f'[Signal] Tags changed on: {instance.title}')