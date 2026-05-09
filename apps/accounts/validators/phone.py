from django.core.validators import RegexValidator 

phone_validator = RegexValidator(
    regex=r'^\+989\d{9}$',
    message=" phone number must be in format +989********* "
)