# edc-death-report


A death model class is declared in your app just like any other CRF where the only difference is the additional foreign key to `RegisteredSubject`:

	from django.db import models
	from edc_base.model.models import BaseUuidModel
	from edc_base.audit_trail import AuditTrail
	from edc_death_report.models import DeathReportMixin
	from edc.entry_meta_data.managers import EntryMetaDataManager
	from edc.subject.registration.models import RegisteredSubject
	from edc_visit_tracking.models import CrfModelMixin
	
	from .subject_visit import SubjectVisit	
	
	class SubjectDeathReport(CrfModelMixin, DeathReportMixin, BaseUuidModel):
	
	    """ A model completed by the user on the subject's death. """
	
	    registered_subject = models.OneToOneField(RegisteredSubject)
	
	    subject_visit = models.OneToOneField(SubjectVisit)
	
	    history = AuditTrail()
	
	    entry_meta_data_manager = EntryMetaDataManager(MaternalVisit)
	
	    class Meta:
	        app_label = 'my_app'
	        verbose_name = "Subject Death Report"
