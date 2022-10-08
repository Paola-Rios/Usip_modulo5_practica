from django.core.exceptions import ValidationError

def validar_nombrePropietario(value):
    if len(value) < 4:
        raise ValidationError("El nombre debe contener al menos cuatro caracteres")

def validar_carnetPropietario(value):
    firstCharacter= value[0]

    if not (firstCharacter.isdigit()):
        raise ValidationError("El carnet no puede empezar con una letra")