from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.http import request


class Goods(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    cost = models.DecimalField(max_digits=6, decimal_places=2,
                               verbose_name='Цена')
    collection = models.ManyToManyField('Collections', verbose_name='Коллекция')

    size_s = models.PositiveSmallIntegerField(editable=True, blank=True, null=True,  verbose_name='Размер S')
    size_m = models.PositiveSmallIntegerField(editable=True, blank=True, null=True, verbose_name='Размер M')
    size_l = models.PositiveSmallIntegerField(editable=True, blank=True, null=True, verbose_name='Размер L')
    size_xl = models.PositiveSmallIntegerField(editable=True, blank=True, null=True, verbose_name='Размер XL')
    photo1 = models.ImageField(upload_to='photos/%m/', blank=True, verbose_name='Фото')
    photo2 = models.ImageField(upload_to='photos/%m/', blank=True, verbose_name='Фото')
    photo3 = models.ImageField(upload_to='photos/%m/', blank=True, verbose_name='Фото')
    photo4 = models.ImageField(upload_to='photos/%m/', blank=True, verbose_name='Фото')
    photo5 = models.ImageField(upload_to='photos/%m/', blank=True, verbose_name='Фото')
    photo6 = models.ImageField(upload_to='photos/%m/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # now_path = request.HttpRequest.get_full_path()
        # collection_slug = str(now_path).split('/')[-2]
        collection = [str(col) for col in self.collection.all()]
        collection_slug = slugify(collection[0])
        return reverse('good', kwargs={'good_slug': self.slug, 'collection_slug': collection_slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']


class Collections(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Наименование коллекции')
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to='img/collections', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collection', kwargs={'collection_slug': self.slug})

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        ordering = ['id']

