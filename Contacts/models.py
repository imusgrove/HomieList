from django.db import models
from django.core.urlresolvers import reverse

class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.IntegerField()
    street_address = models.CharField(max_length=250)
    headshot = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('Contacts:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name

