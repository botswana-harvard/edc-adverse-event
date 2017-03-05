from edc_base.model_mixins import BaseModel, ListModelMixin


class CauseCategory (ListModelMixin, BaseModel):

    class Meta:
        ordering = ['display_index']
        app_label = 'edc_death_report'
