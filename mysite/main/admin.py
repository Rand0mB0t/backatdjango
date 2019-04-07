from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE 
from django.db import models

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    '''
        This class is to modify how our model is presented in the 
        admin interface, we can use fields or fieldsets mutually
        exclusively to order or group the fields
    '''
    # fields = [
    #     "tutorial_title",
    #     "tutorial_content",
    #     "tutorial_published",
    # ]

    fieldsets = (
        ("Title/date", {
            "fields": (
                "tutorial_title",
                "tutorial_published",
            ),
        }),
        ("Content", {
            "fields":(
                "tutorial_content",
            )
        })
    )

    formfield_overrides = {
        models.TextField : {
            'widget' : TinyMCE()
        }
    }
    
admin.site.register(Tutorial, TutorialAdmin)