from dashboard.admin.GenericModelAdmin import GenericModelAdmin


class BILAdmin(GenericModelAdmin):
    search_fields = (
        'bil_number',

    )

    list_display = (
        'bil_number', 'shipping_name', 'created',)
