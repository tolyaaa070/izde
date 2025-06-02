from django.contrib import admin
from .models import (UserProfile,Agent,Amenity,
                     Houses,HousePhotos,
                     Rating)
from modeltranslation.admin import TranslationAdmin


class HousesImageInline(admin.TabularInline):
    model = HousePhotos
    extra = 1


class AmenityInline(admin.TabularInline):
    model = Amenity
    extra = 1

@admin.register(Houses)
class HotelAdmin(TranslationAdmin):
    inlines = [HousesImageInline,AmenityInline]


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Agent)
class AgentAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(HousePhotos)
admin.site.register(Rating)