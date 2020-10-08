from django.db import models

# Create your models here.


class BroadcastType(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)

    class Meta:
        verbose_name = "Broadcast type"
        verbose_name_plural = "Broadcast types"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(BroadcastType, self).save(*args, **kwargs)


class Broadcast(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    date = models.DateTimeField(auto_now=True)
    link = models.URLField()
    broadcast_type = models.ForeignKey(
        BroadcastType, on_delete=models.CASCADE, related_name='type')

    class Meta:
        verbose_name = "Broadcast"
        verbose_name_plural = "Broadcasts"

    def __str__(self):
        return f'{self.title} {self.date}'

    def save(self, *args, **kwargs):
        super(Broadcast, self).save(*args, **kwargs)


class Event(models.Model):
    data = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f'{self.broadcast.title} {self.creation_date}'

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)


class Comment(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='comments', on_delete=models.CASCADE)
    data = models.TextField(max_length=512)
    creation_date = models.DateTimeField(auto_now_add=True)
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user} - {self.broadcast.title}'

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
