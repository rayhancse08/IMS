from dashboard.admin.GenericModelAdmin import GenericModelAdmin


class LCAdmin(GenericModelAdmin):
    search_fields = (
        'lc_number',

    )

    list_display = (
         'lc_number', 'issue_bank', 'issue_date', 'expire_date', 'client_name', 'client_bank_name', 'created',)
