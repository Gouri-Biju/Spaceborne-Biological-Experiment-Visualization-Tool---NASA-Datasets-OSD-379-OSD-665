from django.contrib import admin
from .models import Experiment

class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('experiment_id', 'experiment_name', 'experiment_file')  # Columns to display in the list view
    search_fields = ('experiment_id', 'experiment_name')                     # Fields that can be searched in the admin interface

# Alternatively, you can use the following syntax to register the model
# admin.site.register(Experiment, ExperimentAdmin)


