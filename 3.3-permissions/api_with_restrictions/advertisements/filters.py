from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    status = filters.ModelMultipleChoiceFilter(
        to_field_name='status',
        queryset=Advertisement.objects.all()
    )
    created_at = filters.DateFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at', 'creator']
