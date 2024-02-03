from django.core.exceptions import ValidationError


def char_validator(value):
    if not all(char.isalnum() or char == "_" for char in value):
        raise ValidationError("Username must contain only letters, digits, and underscores!")

