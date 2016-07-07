from edc_base.model.models.list_model_mixin import ListModelMixin
from edc_base.model.models.base_model import BaseModel


class MedicalResponsibility (ListModelMixin, BaseModel):

    class Meta:
        ordering = ['display_index']
        app_label = 'edc_death_report'
