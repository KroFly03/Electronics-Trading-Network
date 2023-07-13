from django.db import models


class Contact(models.Model):
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Улица', max_length=50)
    number = models.CharField(verbose_name='Номер дома', max_length=10)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    model = models.CharField(verbose_name='Модель', max_length=50)
    release_date = models.DateField(verbose_name='Дата выхода на рынок', auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class DefaultNetworkLink(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    contact = models.ForeignKey(Contact, verbose_name='Контакты', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, verbose_name='Продукты')
    created = models.DateField(verbose_name='Время создания', auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Factory(DefaultNetworkLink):
    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class RetailNetwork(DefaultNetworkLink):
    provider = models.ForeignKey(Factory, verbose_name='Поставщик', on_delete=models.CASCADE)
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=20, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class IndividualEntrepreneur(DefaultNetworkLink):
    provider = models.ForeignKey(RetailNetwork, verbose_name='Поставщик', on_delete=models.CASCADE)
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=20, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'
