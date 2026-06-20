import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
phonenumbers.PhoneMetadata.load_all()

telefone = "27 99574 4791"

telefone_ajustado = phonenumbers.parse(telefone, "BR")
local = geocoder.description_for_number(telefone_ajustado, "pt-br")
operadora = carrier.name_for_number(telefone_ajustado, "pt-br")
fuso_horario = timezone.time_zones_for_number(telefone_ajustado)

print(telefone_ajustado)
print(local)
print(operadora)
print(fuso_horario)
