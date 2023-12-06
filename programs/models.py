import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from modelcluster.fields import ParentalKey

from wagtail.api import APIField
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField


class ProgramsIndexPage(Page):
    template = "programs/programs_index_page.html"
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        return context


class ProgramPage(Page):
    template = "programs/program_page.html"
    # max_count = 1

    on_home = models.BooleanField(default=False)
    body = RichTextField(null=True, blank=True,)
    date = models.DateField(_("Post date"), null=True, blank=True,)
    program_image = models.ForeignKey(  # post image 960*480px
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='+',
    )
    feed_image = models.ForeignKey(  # preview image
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('on_home'),
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        FieldPanel('program_image'),
        FieldPanel('feed_image'),
    ]



