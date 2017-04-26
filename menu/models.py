from django.db import models


class BaseAbstractModel(models.Model):
    is_visible = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=10)

    class Meta:
        abstract = True


class Menu(BaseAbstractModel):
    name = models.CharField(max_length=20, verbose_name='Название меню')
    slug = models.SlugField(max_length=255, verbose_name='Идентификатор', null=True)

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'

    def __str__(self):
        return self.name


class MenuParentItem(BaseAbstractModel):
    menu = models.ForeignKey(Menu, related_name='items', verbose_name='меню')
    title = models.CharField(max_length=100, verbose_name='Название пункта')
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', blank=True)

    class Meta:
        verbose_name = 'родительский пункт меню'
        verbose_name_plural = 'родительские пункты меню'
        ordering = ('order', )

    def get_full_url(self):
        if self.slug:
            url = '/{}/'.format(self.slug)
        else:
            url = '/'
        return url

    def __str__(self):
        return self.title


class MenuChildItem(BaseAbstractModel):
    parent = models.ForeignKey(MenuParentItem, related_name='items', verbose_name='роительский пункт')
    title = models.CharField(max_length=100, verbose_name='Название пункта')
    slug = models.SlugField(max_length=255, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'дочерний пункт меню'
        verbose_name_plural = 'дочерние пункты меню'
        ordering = ('order', )

    def get_full_url(self):
        parent_slug = self.parent.slug
        url = '/{}/{}/'.format(parent_slug, self.slug)
        return url

    def __str__(self):
        return self.title

