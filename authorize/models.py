from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Item(models.Model):
  name = models.CharField(_('title'), max_length=255)
  description = models.TextField(_('description'), blank=True, null=True)
  owner = models.ForeignKey('auth.User', verbose_name=_('owner'), related_name='items')
  
  def __str__(self):
    return self.name
