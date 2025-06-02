from .models import Agent, Amenity, Houses
from modeltranslation.translator import TranslationOptions,register

@register(Agent)
class ProductTranslationOptions(TranslationOptions):
    fields = ('position','areas')

@register(Houses)
class HousesTranslationOptions(TranslationOptions):
    fields = ('name_houses','locations')
