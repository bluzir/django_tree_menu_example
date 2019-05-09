from django.db import models
from django.urls import reverse


class BaseAbstractModel(models.Model):
    """
    Base abstract model.
    Provides visibility settings, ordering, and created/updated field.
    """
    is_visible = models.BooleanField(default=True, verbose_name='Visibility')
    order = models.IntegerField(default=10, verbose_name='Order')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Menu(BaseAbstractModel):
    """
    Model for menu item. Has title and slug fields.
    Slug is designed to use in templatetag 'draw menu' for displaying menu
    """
    title = models.CharField(max_length=20, verbose_name='Menu title')
    slug = models.SlugField(max_length=255, verbose_name='Slug', null=True,
                            help_text='Use it in templatetag for displaying menu')
    named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True,
                                 help_text='Named url from your urls.py file')

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return self.title

    def get_full_path(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = '/{}/'.format(self.slug)
        return url


class MenuItem(BaseAbstractModel):
    """
    Model for menu item. Has menu, parent, title, url fields.
    Menu field is only requied for top level items.
    You can provide any item in parent field and it will become relative for this item.
    If you'll use 'named url' field, get_url method will use it firstly to generate url.
    And only then 'url' field.
    """
    menu = models.ForeignKey(Menu, related_name='items',
                             verbose_name='menu', blank=True, null=True,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='items',
                               verbose_name='parent menu item',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Item title')
    url = models.CharField(max_length=255, verbose_name='Link', blank=True)
    named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True,
                                 help_text='Named url from your urls.py file')

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'
        ordering = ('order', )

    def get_url(self):
        if self.named_url:
            url = reverse(self.named_url)
        elif self.url:
            url = self.url
        else:
            url = '/'

        return url

    def __str__(self):
        return self.title

