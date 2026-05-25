from django.core.validators import RegexValidator

name_validator = RegexValidator(
    regex=r'^[\u0600-\u06FF\s]+$',
    message="Name must contain only Persian letters"
)
