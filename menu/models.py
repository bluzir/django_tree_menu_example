from django.db import models


class BaseAbstractModel(models.Model):
    is_visible = models.BooleanField(default=True, verbose_name='видимость')
    order = models.IntegerField(default=10, verbose_name='порядок')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Menu(BaseAbstractModel):
    title = models.CharField(max_length=20, verbose_name='Название меню')
    slug = models.SlugField(max_length=255, verbose_name='Идентификатор', null=True)

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return self.title

    def get_full_url(self):
        return '/{}/'.format(self.slug)


class MenuItem(BaseAbstractModel):
    menu = models.ForeignKey(Menu,
                             related_name='items',
                             verbose_name='меню',
                             blank=True,
                             null=True)

    parent = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='items',
                               verbose_name='родительский пункт')

    title = models.CharField(max_length=100, verbose_name='Название пункта')
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', blank=True)

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'
        ordering = ('order', )

    def get_full_url(self):
        url = '{}/'.format(self.slug)
        parent = self.parent
        while parent:
            url = '{}/{}'.format(parent.slug, url)
            parent = parent.parent
        full_url = '/{}'.format(url)
        return full_url

    def __str__(self):
        return self.title

