from rest_framework import serializers
from timezone_field.backends import get_tz_backend
from timezone_field.rest_framework import TimeZoneSerializerField


class TimeZoneSerializerChoiceField(TimeZoneSerializerField, serializers.ChoiceField):
    """
    This is necessary until the error is fixed
    https://github.com/mfogel/django-timezone-field/issues/69
    """

    def __init__(self, **kwargs):
        self.use_pytz = kwargs.pop("use_pytz", None)
        self.tz_backend = get_tz_backend(use_pytz=self.use_pytz)
        choice = [(tz, tz) for tz in self.tz_backend.base_tzstrs]
        choice.sort()
        super().__init__(choice, **kwargs)
