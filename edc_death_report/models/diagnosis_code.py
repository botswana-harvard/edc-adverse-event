from django.db import models

from edc_base.model_mixins import BaseModel


class DiagnosisCode (BaseModel):

    list_ref = models.CharField(
        verbose_name="List Reference",
        max_length=35)

    code = models.CharField(
        verbose_name="Code",
        max_length=15,
        unique=True)

    short_name = models.CharField(
        verbose_name="Name",
        max_length=35)

    long_name = models.CharField(
        verbose_name="Long Name",
        max_length=255,
        blank=True)

    def __unicode__(self):
        return '{}: {}'.format(self.code, self.short_name)

    class Meta:
        app_label = 'edc_death_report'
