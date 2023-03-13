from django.core.exceptions import ValidationError


def check_is_published(value):
    if value:
        raise ValidationError("Field can`t be True")

