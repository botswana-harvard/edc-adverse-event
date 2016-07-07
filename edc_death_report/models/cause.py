from edc_base.model.models import ListModelMixin


class Cause (ListModelMixin):

    class Meta:
        ordering = ['display_index']
        app_label = 'edc_death_report'
