from dashboard.admin.GenericModelAdmin import GenericModelAdmin


class UserProfileAdmin(GenericModelAdmin):

    @staticmethod
    def username(obj):
        return obj.user.username

    @staticmethod
    def email(obj):
        return obj.user.email

    search_fields = (
        'phone_number',
        'name',
        'user__email',
        'user__id',

    )

    list_display = (
        'id', 'user', 'name', 'phone_number', 'email',)
