from django.contrib import admin
from testapp.models import resultmodel

# Register your models here.
class resultadmin(admin.ModelAdmin):
    class Meta:
        fields =['prn','name','maths','science','english','socialsci','hindi']
        model = resultmodel
    list_display = ('prn','name','maths','science','english','socialsci','hindi')
admin.site.register(resultmodel,resultadmin)