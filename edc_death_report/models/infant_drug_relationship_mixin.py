from django.db import models

from ..choices import DRUG_RELATIONSHIP


class InfantDrugRelationshipMixin(models.Model):

    study_drug_relationship = models.CharField(
        verbose_name="Relationship between the infant\'s death and (CTX vs Placebo)",
        max_length=25,
        choices=DRUG_RELATIONSHIP,
    )

    infant_nvp_relationship = models.CharField(
        verbose_name="Relationship between the infant\'s death and infant extended nevirapine prophylaxis ",
        max_length=25,
        choices=DRUG_RELATIONSHIP,
    )

    haart_relationship = models.CharField(
        verbose_name="Relationship between the infant\'s death and HAART",
        max_length=25,
        choices=DRUG_RELATIONSHIP,
    )

    trad_med_relationship = models.CharField(
        verbose_name="Relationship between the infant\'s death and traditional medicine use",
        max_length=25,
        choices=DRUG_RELATIONSHIP,
    )

    class Meta:
        abstract = True
