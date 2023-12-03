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


class HomePage(Page):
    max_count = 1

    about_channel_title = models.CharField(_("О канале заголовок"), max_length=100, null=True, blank=True,)
    about_channel_text = RichTextField(_("О канале текст"), null=True, blank=True,)
    offer_for_sposnsors_title = models.CharField(_("Для спонсоров заголовок"), max_length=100, null=True, blank=True,)
    offer_for_sposnsors_text = RichTextField(_("Для спонсоров текст"), null=True, blank=True,)
    offer_for_sponsor_img = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.PROTECT, related_name="+")
    offer_for_sponsor_img_name = models.CharField(_("Контакт для спонсоров"), max_length=100,null=True, blank=True,)
    offer_for_sponsor_img_title = models.CharField(_("Контакт для спонсоров менеджер"), max_length=100, null=True, blank=True,)
    offer_for_sponsor_img_email = models.EmailField(_("для спонсоров контактный Email"), null=True, blank=True,)
    distributor_title = models.CharField(_("Дистрибуция заголовок"), max_length=100, null=True, blank=True,)
    distributor_intro = RichTextField(_("Дистрибуция текст"), null=True, blank=True,)
    distributor_name = models.CharField(_("Дистрибутор название"), max_length=100, null=True, blank=True, )
    distributor_address = models.CharField(_("Дистрибутор название"), max_length=100, null=True, blank=True, )
    distributor_phone = models.CharField(_("Дистрибутор телефон"), max_length=25, null=True, blank=True, )
    distributor_email = models.EmailField(_("Дистрибутор email"), null=True, blank=True,)
    social_title = models.CharField(_("Соц.сети название"), max_length=100, null=True, blank=True,)
    social_youtube_img  = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.PROTECT,
                                            related_name="youtube")
    social_youtube_url = models.CharField(_("Youtube адрес"), max_length=255, null=True, blank=True, )
    social_instagram_img = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.PROTECT,
                                             related_name="instagram")
    social_instagram_url = models.CharField(_("Instagram адрес"), max_length=255, null=True, blank=True, )
    social_facebook_img = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.PROTECT,
                                            related_name="facebook")
    social_facebook_url = models.CharField(_("Facebook адрес"), max_length=255, null=True, blank=True, )


    content_panels = Page.content_panels + [
        FieldPanel('about_channel_title'),
        FieldPanel('about_channel_text'),
        FieldPanel('offer_for_sposnsors_title'),
        FieldPanel('offer_for_sposnsors_text'),
        FieldPanel('offer_for_sponsor_img'),
        FieldPanel('offer_for_sponsor_img_name'),
        FieldPanel('offer_for_sponsor_img_title'),
        FieldPanel('offer_for_sponsor_img_email'),
        FieldPanel('distributor_title'),
        FieldPanel('distributor_intro'),
        FieldPanel('distributor_name'),
        FieldPanel('distributor_address'),
        FieldPanel('distributor_phone'),
        FieldPanel('distributor_email'),
        FieldPanel('social_title'),
        FieldPanel('social_youtube_img'),
        FieldPanel('social_youtube_url'),
        FieldPanel('social_instagram_img'),
        FieldPanel('social_instagram_url'),
        FieldPanel('social_facebook_img'),
        FieldPanel('social_facebook_url'),
    ]