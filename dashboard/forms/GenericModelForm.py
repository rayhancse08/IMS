from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.forms import ModelForm, ModelChoiceField


class GenericModelForm(ModelForm):
    fields_to_wrap_with_related_widget_wrapper = []

    def __init__(self, *args, **kwargs):
        super(GenericModelForm, self).__init__(*args, **kwargs)

        for field in self.fields_to_wrap_with_related_widget_wrapper:
            if field in self.fields:
                self.fields[field] = self.wrap_with_related_field_widget(field)

    def wrap_with_related_field_widget(self, field, widget=ModelChoiceField, can_change_related=True):
        return widget(
            required=self.fields[field].required,
            queryset=self.fields[field].queryset,
            widget=RelatedFieldWidgetWrapper(
                self.fields[field].widget,
                self._meta.model._meta.get_field(field).remote_field,
                self.admin_site,
                can_change_related=can_change_related
            )
        )
