from django.contrib.gis.db import models
from django.contrib.gis.db.models.sql.query import ALL_TERMS

from django_filters import FilterSet

from .filters import GeometryFilter

class GeoFilterSet(FilterSet):
    GEOFILTER_FOR_DBFIELD_DEFAULTS = {
        models.GeometryField: {
            'filter_class': GeometryFilter
        },
    }
    LOOKUP_TYPES = sorted(ALL_TERMS)

    def __init__(self, *args, **kwargs):
        self.filter_overrides.update(self.GEOFILTER_FOR_DBFIELD_DEFAULTS)
        return super(GeoFilterSet, self).__init__(*args, **kwargs)
