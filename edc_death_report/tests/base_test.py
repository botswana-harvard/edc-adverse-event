from __future__ import print_function

from datetime import date
from dateutil.relativedelta import relativedelta

from django.test import TestCase

from edc.subject.lab_tracker.classes import site_lab_tracker
from edc_appointment.models import Appointment
from edc_consent.models.consent_type import ConsentType
from edc_constants.constants import MALE
from edc_lab.lab_profile.classes import site_lab_profiles
from edc_lab.lab_profile.exceptions import AlreadyRegistered as AlreadyRegisteredLabProfile
from edc_registration.tests.factories import RegisteredSubjectFactory
from edc_testing.classes import TestAppConfiguration
from edc_testing.classes import TestLabProfile
from edc_testing.tests.factories import TestConsentWithMixinFactory
from edc_visit_schedule.models import VisitDefinition

from .test_visit_schedule import TestVisitSchedule


class BaseTest(TestCase):

    def setUp(self):
        try:
            site_lab_profiles.register(TestLabProfile())
        except AlreadyRegisteredLabProfile:
            pass
        site_lab_tracker.autodiscover()

        self.configuration = TestAppConfiguration()
        self.configuration.prepare()
        consent_type = ConsentType.objects.first()
        consent_type.app_label = 'edc_testing'
        consent_type.model_name = 'testconsentwithmixin'
        consent_type.save()

        TestVisitSchedule().build()

        self.study_site = '40'
        self.identity = '111111111'
        self.visit_definition = VisitDefinition.objects.get(code='1000')
        subject_identifier = '999-100000-1'
        self.registered_subject = RegisteredSubjectFactory(
            subject_identifier=subject_identifier)
        self.test_consent = TestConsentWithMixinFactory(
            registered_subject=self.registered_subject,
            gender=MALE,
            dob=date.today() - relativedelta(years=35),
            study_site=self.study_site,
            identity=self.identity,
            confirm_identity=self.identity,
            subject_identifier='999-100000-1')
        self.appointment_count = VisitDefinition.objects.all().count()
        self.appointment = Appointment.objects.get(
            registered_subject=self.registered_subject,
            visit_definition=self.visit_definition)
