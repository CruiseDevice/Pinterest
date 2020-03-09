from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class Pin(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='pins_created'
	)
	title=models.CharField(max_length=200)
	slug=models.SlugField(max_length=200,blank=True)
	url=models.URLField(blank=True)
	image=models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True, default='')
	created=models.DateField(auto_now_add=True,db_index=True)

	user_like = models.ManyToManyField(
		settings.AUTH_USER_MODEL, related_name='images_liked',
		blank=True
	)

	def save(self, *args, **kwargs):
	    if not self.slug:
	        self.slug = slugify(self.title)
	    super(Pin, self).save(*args, **kwargs)
	
	def get_absolute_url(self):
		return reverse('pinterest:detail',args=[self.id,self.slug])

	def __str__(self):
		return self.title
