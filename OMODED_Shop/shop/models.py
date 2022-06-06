from django.db import models
from django.urls import reverse


class Goods(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    cost = models.DecimalField(max_digits=6, decimal_places=2,
                               verbose_name='Цена')
    collection = models.ManyToManyField('Collections', verbose_name='Коллекция')
    size_s = models.PositiveSmallIntegerField(editable=True, blank=True, null=True,  verbose_name='Размер S')
    size_m = models.PositiveSmallIntegerField(editable=True, blank=True, null=True,verbose_name='Размер M')
    size_l = models.PositiveSmallIntegerField(editable=True, blank=True, null=True, verbose_name='Размер L')
    size_xl = models.PositiveSmallIntegerField(editable=True, blank=True, null=True, verbose_name='Размер XL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('good', kwargs={'good_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']


class Collections(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name='Наименование коллекции')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('collection', kwargs={'collection_slug': self.slug})

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        ordering = ['id']


class Photos(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.PROTECT,
                             verbose_name='Товар')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/',
                              verbose_name='Фото')

    def __str__(self):
        return self.good

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'
        ordering = ['id']


# class Clients(models.Model):
#     first_name = models.CharField(max_length=20, verbose_name='Имя')
#     last_name = models.CharField(max_length=20, verbose_name='Фамилия')
#     email = models.EmailField(unique=True, verbose_name='E-mail')
#     password = models.CharField(max_length=20, verbose_name='Пароль')
#     address = models.ForeignKey('Addresses', on_delete=models.SET_NULL, null=True,
#                                 verbose_name='Адрес')
#
#     def __str__(self):
#         return '{0} {1}'.format(self.first_name, self.last_name)
#
#     class Meta:
#         verbose_name = 'Клиент'
#         verbose_name_plural = 'Клиенты'
#         ordering = ['id']
#
#
# class Addresses(models.Model):
#     company = models.CharField(max_length=60, blank=True,
#                                verbose_name='Компания')
#     address1 = models.CharField(max_length=255,
#                                 verbose_name='Первый адрес')
#     address2 = models.CharField(max_length=255,
#                                 verbose_name='Второй адрес')
#     city = models.CharField(max_length=100, verbose_name='Город')
#     country = models.ForeignKey('Countries', on_delete=models.SET_NULL, null=True,
#                                 verbose_name='Страна')
#     province = models.ForeignKey('Provinces', on_delete=models.SET_NULL, null=True,
#                                  verbose_name='Регион')
#
#     def __str__(self):
#         return self.address1
#
#     class Meta:
#         verbose_name = 'Адрес'
#         verbose_name_plural = 'Адреса'
#         ordering = ['id']
#
#
# class Countries(models.Model):
#     name = models.CharField(max_length=50, unique=True,
#                             verbose_name='Название страны')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Страна'
#         verbose_name_plural = 'Страны'
#         ordering = ['id']
#
#
# class Provinces(models.Model):
#     country = models.ForeignKey(Countries, on_delete=models.SET_NULL,
#                                 blank=True, null=True,
#                                 verbose_name='Страна')
#     province = models.CharField(max_length=50, unique=True,
#                                 verbose_name='Название региона')
#
#     def __str__(self):
#         return self.province
#
#     class Meta:
#         verbose_name = 'Регион'
#         verbose_name_plural = 'Регионы'
#         ordering = ['id']


class Cart(models.Model):
    from django.contrib.auth.models import User
    client = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Клиент')
    good = models.ManyToManyField(Goods,
                                  verbose_name='Товар')

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['id']


class Order(models.Model):
    from django.contrib.auth.models import User
    client = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Клиент')
    good = models.ManyToManyField(Goods,
                                  verbose_name='Товар')

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['id']