from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms


class NewsFilter(FilterSet):
    pub_time__gt = DateFilter(
        field_name='created',
        label='Created at',
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ),
        lookup_expr='date__gte'
    )

    class Meta:
        model = Post

        fields = {
            # поиск по
            'author': ['exact'],
            'title': ['icontains'],

        }
