from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class ServiceIndexPage(Page):
    subpage_types = ['ServicePage', 'ServiceWithFeePage']


class ServiceAbstractPage(Page):
    """ Holds all fields that are shared accross all service models. """
    featured_image = models.ImageField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("featured_image"),
        FieldPanel("content"),
    ]

    subpage_types = ['ProductPage']

    class Meta:
        abstract = True


class ServicePage(ServiceAbstractPage):
    pass


class ServiceWithFeePage(ServiceAbstractPage):
    fee_price = models.DecimalField(max_digits=4, decimal_places=2)

    content_panels = ServiceAbstractPage.content_panels + [
        FieldPanel("fee_price")
    ]