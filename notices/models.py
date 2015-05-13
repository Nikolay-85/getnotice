from django.db import models
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    text = models.CharField(max_length=255, verbose_name=_('Text'))
