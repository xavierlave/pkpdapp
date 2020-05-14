from django.db import models
from .validators import validate_file_extension

# Create your models here.

class KeyWords(models.Model):
    key_word = models.CharField(max_length=200)

    class Meta:
        ordering = ['key_word']

    def __str__(self):
        return self.key_word


class TermsOfDistribution(models.Model):
    terms = models.CharField(max_length=200)

    class Meta:
        ordering = ['terms']

    def __str__(self):
        return self.terms


class Annotations(models.Model):
    model_name = models.CharField(max_length=200) 
    reference = models.CharField(max_length=2083)
    version = models.FloatField()
    creation_date = models.DateTimeField('Date Created')
    author_name = models.CharField(max_length=400)
    author_contact = models.CharField(max_length=200)
    terms_of_dist = models.ManyToManyField(TermsOfDistribution)
    num_compartments = models.PositiveSmallIntegerField()
    application = models.ManyToManyField(KeyWords)
    sbml_file = models.TextField() 

    class Meta:
        ordering = ['author_name']

    def __str__(self):
        return self.model_name



class ModelFile(models.Model):
    model = models.FileField(validators=[validate_file_extension])

    def save(self, *args, **kwargs):
        super(ModelFile, self).save(*args, **kwargs)
        filename = self.data.url


