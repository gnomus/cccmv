from django.db import models

# Create your models here.


class Erfa(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    anschrift = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Mitglied(models.Model):
    def __str__(self):
        return str(self.chaosnummer) + ': ' + self.vorname + ' ' + self.nachname
    chaosnummer = models.IntegerField(default=0)
    vorname = models.CharField(max_length=200)
    nachname = models.CharField(max_length=200)
    anschrift = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    erfa = models.ForeignKey(Erfa)

