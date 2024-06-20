from django.contrib import admin
from .models import StudentApplication, OCData, OCBureauLeaderData
# Register your models here.

admin.site.register(StudentApplication)
admin.site.register(OCData)
admin.site.register(OCBureauLeaderData)