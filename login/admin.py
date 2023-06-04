from django.contrib import admin
from login.models import Food_request,Services,Leave,Contact,Laundry
# Register your models here.
admin.site.register(Food_request)
admin.site.register(Services) 
admin.site.register(Leave)
admin.site.register(Contact)
admin.site.register(Laundry)