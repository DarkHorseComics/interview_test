from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Contributor(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    series = models.ForeignKey(Series)
    issue_number = models.PositiveIntegerField()
    cover_image = models.URLField()
    writers = models.ManyToManyField(Contributor, related_name='writer_books')
    artists = models.ManyToManyField(Contributor, related_name='artist_books')

    class Meta:
        ordering = ['series__name', 'issue_number']

    def __unicode__(self):
        return self.name