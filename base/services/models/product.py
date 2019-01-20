from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page


class ProductPage(Page):
    featured_image = models.ImageField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("featured_image", classname="full"),
                FieldPanel("content", classname="full"),
            ],
            heading="Main information",
            classname="collapsible collapsed"
        ),
    ]

    @property
    def service(self):
        return self.get_parent()