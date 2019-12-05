from django.db import models
from django.utils.translation import gettext as _
#gettext:can write strings at any language we want
#can run a command to search all the strings
#for translators to translate the strings.
#So we can have ea multilingual application easily.

# Create your models here.
class Pet(models.Model):
    species = models.CharField(
            help_text=_('Species of animal'),
            max_length = 50,
    )
    
    name = models.CharField(
            help_text=_('Name of Pet'),
            max_length = 100,
    )

    birth_date = models.DateField(
            help_text=_('Birth Date'),
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    SEX_CHOICES = (
            (MALE, 'Male'),
            (FEMALE,'Female'),
            (OTHER,'Other'),
    )

    sex = models.CharField(
            help_text=_('Sex of pet'),
            max_length=16, # no need of that large
            choices = SEX_CHOICES,
            default=OTHER, # default choice
    )

    def __str__(self):
        return self.name
