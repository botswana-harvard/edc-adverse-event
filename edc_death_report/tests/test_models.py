from __future__ import print_function

from django import forms
from django.db import models

from edc.entry_meta_data.models import MetaDataMixin
from edc.subject.registration.models.registered_subject import RegisteredSubject
from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_death_report.forms.death_report_form_mixin import DeathReportFormMixin
from edc_death_report.models.death_report_mixin import DeathReportModelMixin
from edc_offstudy.models import OffStudyModelMixin, OffStudyMixin
from edc_visit_tracking.models import BaseVisitTracking, PreviousVisitMixin, CrfModelMixin


class TestVisitModel(OffStudyMixin, MetaDataMixin, PreviousVisitMixin, BaseVisitTracking):

    OFF_STUDY_MODEL = ('edc_death_report', 'OffStudyModel')

    REQUIRES_PREVIOUS_VISIT = True

    def get_subject_identifier(self):
        return self.appointment.registered_subject.subject_identifier

    def custom_post_update_entry_meta_data(self):
        pass

    def get_requires_consent(self):
        return False

    class Meta:
        app_label = 'edc_death_report'


class OffStudyModel(CrfModelMixin, OffStudyModelMixin, BaseUuidModel):

    registered_subject = models.OneToOneField(RegisteredSubject)

    test_visit_model = models.OneToOneField(TestVisitModel)

    class Meta:
        app_label = 'edc_death_report'


class DeathReport(CrfModelMixin, DeathReportModelMixin, BaseUuidModel):

    registered_subject = models.OneToOneField(RegisteredSubject)

    test_visit_model = models.OneToOneField(TestVisitModel)

    class Meta:
        app_label = 'edc_death_report'


class DeathReportForm(DeathReportFormMixin, forms.ModelForm):

    class Meta:
        model = DeathReport
        fields = '__all__'
