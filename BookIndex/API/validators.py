from django.core.exceptions import ValidationError


def PublishingValidator(value):
    if not 868 <= value and value >= 2021:
        raise ValidationError("Wrong publishing year")