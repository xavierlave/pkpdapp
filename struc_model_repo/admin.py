from django.contrib import admin
from .models import KeyWords, TermsOfDistribution, Annotations, ModelFile

# Register your models here.

admin.site.register(KeyWords)
admin.site.register(TermsOfDistribution)
admin.site.register(Annotations)
admin.site.register(ModelFile)
