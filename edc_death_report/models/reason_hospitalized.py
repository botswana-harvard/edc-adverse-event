from edc_base.model.models.base_list_model import BaseListModel


class ReasonHospitalized (BaseListModel):
    class Meta:
        ordering = ['display_index']
        app_label = 'edc_adverse_event'
