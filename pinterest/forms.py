from urllib import request

from django import forms
from django.core.files.base import ContentFile
from django.utils import slugify

from .models import Pin


class PinCreateForm(forms.ModelForm):
	class Meta:
		model = Pin

		fields = ('title','url')
		
	def clean_url(self):
		url = self.cleaned_data['url']
		valid_extensions = ['jpg','jpeg']
		extension = url.rsplit('.',1)[1].lower()
		if extension not in valid_extensions:
			raise.forms.ValidationError('The given URL does not match valid \
							image extensions')

	def save(self, force_insert=False, force_update=False, commit=True):
		image =super(PinCreateForm, self).save(commit=False)
		image_url = self.cleaned_data['url']
		image_name = '{}.{}'.format(slugify(image.title),\
											image_url.rsplit(',',1)[1].lower())
		# download the image from the given url
		response = request.urlopen(image_url)
		image.image.save(image_name,ContentFile(response.read()),save=False)

		if commit:
			image.save()
		return image