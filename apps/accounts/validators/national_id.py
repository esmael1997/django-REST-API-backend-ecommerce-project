from django.core.validators import RegexValidator

national_id_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="National ID must be exactly 10 digits"
) 
