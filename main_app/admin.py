from django.contrib import admin
from .models import Relation, Communication, Activity, Photo

# Register your models here.
admin.site.register(Relation)
admin.site.register(Communication)
admin.site.register(Activity)
admin.site.register(Photo)