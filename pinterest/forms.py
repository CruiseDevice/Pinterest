from urllib import request

from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Pin


default_img = 'http://saveabandonedbabies.org/wp-content/uploads/2015/08/default.png'


class PinCreateForm(forms.ModelForm):
    class Meta:
        model = Pin

        fields = ('title', 'url')

    def clean_url(self):
        if self.cleaned_data['url']:
            url = self.cleaned_data['url']
        else:
            url = default_img
        print('url:', url)

        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid \
                            image extensions')
        return url

    def save(self, force_insert=False, force_update=False, commit=False):
        image = super(PinCreateForm, self).save(commit=False)
        if self.cleaned_data['url'] is None:
            image_url = default_img
        else:
            image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),
                                    image_url.rsplit('.', 1)[1].lower())

        # download image from the given URL
        response = request.urlopen(image_url)
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)

        if commit:
            image.save()
        return image
