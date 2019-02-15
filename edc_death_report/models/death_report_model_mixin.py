from django.db import models
from edc_constants.choices import YES_NO

from edc_base.model.fields import OtherCharField
from edc_base.model.validators.date import date_not_before_study_start, date_not_future

from .cause import Cause
from .cause_category import CauseCategory
from .diagnosis_code import DiagnosisCode
from .medical_responsibility import MedicalResponsibility
from .reason_hospitalized import ReasonHospitalized


class DeathReportModelMixin(models.Model):

    death_date = models.DateField(
        verbose_name="Date of Death:",
        validators=[
            date_not_before_study_start,
            date_not_future])

    cause = models.ForeignKey(
        to=Cause,
        verbose_name=(
            'What is the primary source of cause of death information? '
            '(if multiple source of information, '
            'list one with the smallest number closest to the top of the list) '))

    cause_other = OtherCharField(
        verbose_name="if other specify...",
        blank=True,
        null=True)

    death_cause = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name=(
            'Describe the major cause of death(including pertinent autopsy information '
            'if available),starting with the first noticeable illness thought to be '
            'related to death,continuing to time of death.'),
        help_text=(
            'Note: Cardiac and pulmonary arrest are not major reasons and should not '
            'be used to describe major cause'))

    cause_category = models.ForeignKey(
        to=CauseCategory,
        verbose_name=("Based on the above description, what category "
                      "best defines the major cause of death? "),
        help_text="")

    cause_category_other = OtherCharField(
        verbose_name="if other specify...",
        blank=True,
        null=True)

    participant_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Was the participant hospitalised before death?")

    reason_hospitalized = models.ForeignKey(
        ReasonHospitalized,
        verbose_name="if yes, hospitalized, what was the primary reason for hospitalisation? ",
        help_text="",
        blank=True,
        null=True)

    reason_hospitalized_other = models.TextField(
        verbose_name=("if other illness or pathogen specify or non "
                      "infectious reason, please specify below:"),
        max_length=250,
        blank=True,
        null=True)

    days_hospitalized = models.IntegerField(
        verbose_name=(
            "For how many days was the participant hospitalised during "
            "the illness immediately before death? "),
        help_text="in days",
        default=0)

    comment = models.TextField(
        max_length=500,
        verbose_name="Comments",
        blank=True,
        null=True)

    illness_duration = models.IntegerField(
        verbose_name="Duration of acute illness directly causing death   ",
        help_text="in days (If unknown enter -1)")

    perform_autopsy = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name="Will an autopsy be performed later  ")

    diagnosis_code = models.ForeignKey(
        DiagnosisCode,
        max_length=25,
        blank=True,
        null=True,
        verbose_name="Please code the cause of death as one of the following:",
        help_text="Use diagnosis code from Diagnosis Reference Listing")

    diagnosis_code_other = OtherCharField(
        verbose_name="if other specify...",
        blank=True,
        null=True)

    medical_responsibility = models.ForeignKey(
        MedicalResponsibility,
        verbose_name=(
            "Who was responsible for primary medical care of the "
            "participant during the month prior to death?"),
        help_text="")

    class Meta:
        abstract = True
