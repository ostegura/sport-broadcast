from django.contrib.auth.models import Group
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_rest_permission.settings')


django.setup()


GROUPS = ['admin', 'moderator', 'user']
MODELS = ['user', 'Broadcast type', 'Broadcast', 'Event', 'Comment']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
