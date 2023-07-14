import phonenumbers
from phonenumbers import geocoder

phonenumber_1=phonenumbers.parse('+917380150117')
print(geocoder.description_for_number(phonenumber_1,"en"));