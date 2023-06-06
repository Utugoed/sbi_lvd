from django.db import models
from django.utils.html import format_html

from organisations.models import Organisation
from users.models import CustomUser


def event_file(instance, filename):
    return '/'.join(['events', 'images', f'{str(instance.id)}_{filename}'])


class Event(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    organisations = models.ManyToManyField(Organisation)
    image = models.ImageField(upload_to=event_file)
    date = models.DateTimeField()

    def __repr__(self):
        return f"{self.title} - {self.date} - {self.organisations}"

    @classmethod
    def get_queryset(cls):
        users_prefetch = models.Prefetch(
            'users',
            queryset=CustomUser.objects.all()
        )
        organisations_prefetch = models.Prefetch(
            'organisations',
            queryset=Organisation.objects.prefetch_related(users_prefetch).all(),
        )
        queryset = cls.objects.prefetch_related(organisations_prefetch).all()
        return queryset
