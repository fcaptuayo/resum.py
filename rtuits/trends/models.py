from django.db import models
from django.core.urlresolvers import reverse
from djangotoolbox.fields import ListField, EmbeddedModelField
from datetime import datetime  

class Trend(models.Model):
	url = models.TextField()
	query = models.TextField()
	date_modified = models.DateTimeField(default=datetime.now, blank=True)
	name = models.TextField()
	def get_absolute_url(self):
		return reverse('trend', kwargs={"slug": self.name})
	def __unicode__(self):
		return self.name



