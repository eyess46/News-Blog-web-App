from django.contrib import admin
from .models import News, Contactform, Sport, Politics, Business

# Register your models here.
admin.site.register(News)
admin.site.register(Sport)
admin.site.register(Politics)
admin.site.register(Business)
admin.site.register(Contactform)
