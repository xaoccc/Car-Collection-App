from django.core.exceptions import ValidationError


def char_validator(value):
    if not all(char.isalnum() or char == "_" for char in value):
        raise ValidationError("Username must contain only letters, digits, and underscores!")

def name_validator(value):
    if not value.isalpha():
        raise ValidationError("Name must contain only letters!")
    if len(value) < 2:
        raise ValidationError("Name must be at least 2 characters long!")
    if len(value) > 20:
        raise ValidationError("Name must be at most 20 characters long!")
    if not value[0].isupper():
        raise ValidationError("Name must start with an uppercase letter!")
    if not value[1:].islower():
        raise ValidationError("Name can have just one uppercase letter!")

def password_validator(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters long!")
    if not any(char.isdigit() for char in value):
        raise ValidationError("Password must contain at least one digit!")
    if not any(char.isupper() for char in value):
        raise ValidationError("Password must contain at least one uppercase letter!")
    if not any(char.islower() for char in value):
        raise ValidationError("Password must contain at least one lowercase letter!")
    if not any(char in "!@#$%^&*()_+{}:<>?/.,;'" for char in value):
        raise ValidationError("Password must contain at least one special character!")