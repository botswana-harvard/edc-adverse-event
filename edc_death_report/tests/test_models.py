from __future__ import print_function

from django import forms
from django.db import models

from edc_meta_data.models import CrfMetaDataMixin
from edc_base.model.models import BaseUuidModel
from edc_death_report.forms import DeathReportFormMixin
from edc_death_report.models import DeathReportModelMixin
from edc_offstudy.models import OffStudyModelMixin, OffStudyMixin
from edc_visit_tracking.models import VisitModelMixin, PreviousVisitMixin, CrfModelMixin


class TestDeathVisitModel(OffStudyMixin, CrfMetaDataMixin, PreviousVisitMixin, VisitModelMixin):

    off_study_model = ('edc_death_report', 'OffStudyModel')

    REQUIRES_PREVIOUS_VISIT = True

    def get_subject_identifier(self):
        return self.appointment.registered_subject.subject_identifier

    def get_requires_consent(self):
        return False

    class Meta:
        app_label = 'edc_death_report'


class OffStudyModel(CrfModelMixin, OffStudyModelMixin, BaseUuidModel):

    test_visit_model = models.OneToOneField(TestDeathVisitModel)

    class Meta:
        app_label = 'edc_death_report'


class DeathReport(CrfModelMixin, DeathReportModelMixin, BaseUuidModel):

    test_visit_model = models.OneToOneField(TestDeathVisitModel)

    class Meta:
        app_label = 'edc_death_report'


class DeathReportForm(DeathReportFormMixin, forms.ModelForm):

    class Meta:
        model = DeathReport
        fields = '__all__'
