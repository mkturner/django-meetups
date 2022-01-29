from django.contrib import admin

# import model to register them
from .models import Meet

# Define custom columns for 
class MeetAdmin(admin.ModelAdmin):
    # list display accepts a tuples of properties that you want displayed
    # as columns in the admin   
    list_display = ('title', 'slug', 'location',)
    list_filter = ('location',)
    # automatically populate fields of new items based on other data
    # accepts a dictionary
    prepopulated_fields = {
        # Each key accepts a tuple of values to be concatenated as value
        'slug': ('title',)
        # because slug is a SlugField django will transform it automatically
    }

# Register your models here.
admin.site.register(Meet, MeetAdmin)

